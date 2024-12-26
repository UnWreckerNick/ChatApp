const ws = new WebSocket("ws://127.0.0.1:8000/ws/chat");

ws.onopen = () => {
    console.log("Connected to WebSocket");
    ws.send(JSON.stringify({ message: "Hello, Server!" }));
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log("Message from server:", data);
};

ws.onclose = () => {
    console.log("Disconnected from WebSocket");
};
