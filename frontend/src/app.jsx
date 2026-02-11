import { useState } from "react";
import { askQuestion } from "./services/api";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import Sidebar from "./components/Sidebar";
import "./index.css";

function App() {
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [darkMode, setDarkMode] = useState(false);

    const handleSend = async (text) => {
        const newMessages = [...messages, { role: "user", content: text }];
        setMessages(newMessages);
        setLoading(true);

        try {
            const response = await askQuestion(text);

            setMessages([
                ...newMessages,
                { role: "assistant", content: response.data.answer },
            ]);
        } catch (error) {
            console.error(error);
        }

        setLoading(false);
    };

    return (
        <div className={`app-container ${darkMode ? "dark" : ""}`}>

            <Sidebar darkMode={darkMode} setDarkMode={setDarkMode} />

            <div className="chat-container">
                <ChatWindow messages={messages} loading={loading} />
                <ChatInput onSend={handleSend} />
            </div>
        </div>
    );
}

export default App;
