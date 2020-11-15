import time
from models.Model import Model
from sklearn.svm import SVC, LinearSVC


class SupportVectorMachine(Model):

    def svm_rbf(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC()
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_rbf_gammaAuto(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(gamma='auto')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_rbf_CMin(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(C=1e-2)
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_rbf_CMax(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(C=1e2)
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_poly(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(kernel='poly')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_poly_gammaAuto(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(kernel='poly', gamma='auto')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_sigmoid(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(kernel='sigmoid')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_sigmoid_gammaAuto(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(kernel='sigmoid', gamma='auto')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_linear(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(kernel='linear')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump

    def svm_precomputed(self):
        print("SupportVectorMachine")
        start_time = time.process_time()

        model = SVC(kernel='precomputed')
        score, predictions = self.runClassifier(model)
        model_dump = f'{time.process_time()}-default-svm.joblib'

        elapsed_time = time.process_time() - start_time

        return score, elapsed_time, predictions, model_dump
