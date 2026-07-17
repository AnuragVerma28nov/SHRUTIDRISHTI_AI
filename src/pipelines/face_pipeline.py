import dlib
import numpy as np
import streamlit as st
import face_recognition_models
from sklearn.svm import SVC
from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    # Ensure correct dtype
    if image_np.dtype != np.uint8:
        image_np = image_np.astype(np.uint8)

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)

        # Correct method name (without underscore)
        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        encodings.append(np.array(face_descriptor))

    return encodings


@st.cache_resource
def get_trained_model():
    X = []
    y = []

    # Call function properly
    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get("face_embedding")

        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(X) == 0:
        return None

    try:
        clf = SVC(
            kernel="linear",
            probability=True,
            class_weight="balanced"
        )

        clf.fit(X, y)

        return {
            "clf": clf,
            "X": X,
            "y": y
        }

    except Exception as e:
        print(f"Training Error: {e}")
        return None


def train_classifier():
    st.cache_resource.clear()

    model_data = get_trained_model()

    return model_data is not None


def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_students = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_students, [], len(encodings)

    clf = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        if len(all_students) >= 2:
            predicted_id = clf.predict([encoding])[0]
        else:
            predicted_id = all_students[0]

        try:
            idx = y_train.index(predicted_id)
            student_embedding = X_train[idx]

            distance = np.linalg.norm(
                student_embedding - encoding
            )

            resemblance_threshold = 0.6

            if distance <= resemblance_threshold:
                detected_students[int(predicted_id)] = True

        except Exception:
            continue

    return detected_students, all_students, len(encodings)