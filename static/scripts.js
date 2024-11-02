function makePrediction() {
    const defesa = document.getElementById("defesa").value;
    const pocoes = document.getElementById("pocoes").value;
    const transfiguracao = document.getElementById("transfiguracao").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            DefesaContraArtes: defesa,
            Pocoes: pocoes,
            Transfiguracao: transfiguracao
        })
    })
    .then(response => {
        if (!response.ok) throw new Error("Dados inválidos");
        return response.json();
    })
    .then(data => {
        document.getElementById("prediction-result").innerText = "Nota Final Prevista: " + data.predicao.toFixed(2);
    })
    .catch(error => {
        document.getElementById("prediction-result").innerText = "Erro: " + error.message;
    });
}
