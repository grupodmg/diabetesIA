class DiabetesForm extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
            <style>
                form {
                    display: flex;
                    flex-direction: column;
                    max-width: 300px;
                    margin: auto;
                }
                label {
                    margin: 5px 0;
                }
                input {
                    margin-bottom: 10px;
                    padding: 5px;
                }
                button {
                    padding: 10px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
            </style>
            <form id="diabetesForm">
                <label for="pregnancies">Embarazos:</label>
                <input type="number" id="pregnancies" name="Pregnancies" required>

                <label for="glucose">Glucosa:</label>
                <input type="number" id="glucose" name="Glucose" required>

                <label for="bloodPressure">Presión Sanguínea:</label>
                <input type="number" id="bloodPressure" name="BloodPressure" required>

                <label for="skinThickness">Grosor de Piel:</label>
                <input type="number" id="skinThickness" name="SkinThickness" required>

                <label for="insulin">Insulina:</label>
                <input type="number" id="insulin" name="Insulin" required>

                <label for="bmi">Índice de Masa Corporal (BMI):</label>
                <input type="number" step="0.1" id="bmi" name="BMI" required>

                <label for="diabetesPedigreeFunction">Función de Pedigrí de Diabetes:</label>
                <input type="number" step="0.01" id="diabetesPedigreeFunction" name="DiabetesPedigreeFunction" required>

                <label for="age">Edad:</label>
                <input type="number" id="age" name="Age" required>

                <button type="button" id="submitButton">Continuar</button>
            </form>
            <div id="result"></div>
        `;
    }

    connectedCallback() {
        this.shadowRoot.querySelector('#submitButton').addEventListener('click', () => this.handleSubmit());
    }

    async handleSubmit() {
        const form = this.shadowRoot.querySelector('#diabetesForm');
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Convertir valores a números
        for (let key in data) {
            data[key] = parseFloat(data[key]);
        }

        try {
            const response = await fetch('https://diabetesia.onrender.com/predict', { // Reemplaza con tu URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            this.shadowRoot.querySelector('#result').textContent = 
                result.hasDiabetes ? 'El paciente tiene diabetes.' : 'El paciente no tiene diabetes.';
        } catch (error) {
            this.shadowRoot.querySelector('#result').textContent = 'Error al procesar la solicitud.';
            console.error(error);
        }
    }
}

customElements.define('diabetes-form', DiabetesForm);