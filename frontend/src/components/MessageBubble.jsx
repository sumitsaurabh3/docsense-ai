import { TypeAnimation } from "react-type-animation";
import ReactMarkdown from "react-markdown";

export default function MessageBubble({ role, content }) {
    const isTyping = content === "Typing...";

    return (
        <div className={`message-row ${role}`}>
            <div className={`message-bubble ${role}`}>
                {isTyping ? (
                    <TypeAnimation
                        sequence={["Typing...", 1000, "Typing..", 1000, "Typing...", 1000]}
                        wrapper="span"
                        speed={50}
                        repeat={Infinity}
                    />
                ) : (
                    <ReactMarkdown>{content}</ReactMarkdown>
                )}
            </div>
        </div>
    );
}
