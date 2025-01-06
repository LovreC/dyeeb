function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chat-window").innerHTML += `<p>User: ${userInput}</p>`;
        document.getElementById("chat-window").innerHTML += `<p>Bot: ${data.response}</p>`;
        document.getElementById("user-input").value = "";
    });
}
