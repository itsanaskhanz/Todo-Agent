import React, { useState, useRef, useEffect } from "react";
import { IoSend } from "react-icons/io5";
import { FaTwitter, FaGithub, FaDiscord, FaRobot } from "react-icons/fa";
import "./index.css";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);
  const apiUrl = import.meta.env.VITE_API_URL;

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, newMsg]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(`${apiUrl}/agent`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input }),
      });
      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { role: "agent", text: data.response },
      ]);
    } catch (err) {
      console.error("Error sending message:", err);
      setMessages((prev) => [
        ...prev,
        { role: "agent", text: "Sorry, I encountered an error. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gradient-to-br from-gray-50 to-gray-100 p-4 md:p-6">
      {/* Floating Social Links */}
      <div className="fixed top-1/2 -translate-y-1/2 left-4 md:left-6 flex flex-col gap-3 z-50
          max-md:-left-16 hover:max-md:left-4 transition-all duration-300 group">
        {[
          { href: "https://twitter.com/itsanaskhanz", icon: FaTwitter, color: "text-blue-400 hover:text-blue-500" },
          { href: "https://github.com/itsanaskhanz", icon: FaGithub, color: "text-gray-700 hover:text-gray-900" },
          { href: "https://discord.com/users/itsanaskhanz", icon: FaDiscord, color: "text-indigo-500 hover:text-indigo-600" },
        ].map(({ href, icon: Icon, color }, i) => (
          <a
            key={i}
            href={href}
            target="_blank"
            rel="noopener noreferrer"
            className={`p-2.5 bg-white/90 backdrop-blur-sm rounded-full shadow-sm hover:shadow-md transition-all hover:-translate-y-0.5 ${color}`}
            aria-label={`Link to ${href}`}
          >
            <Icon className="w-4 h-4 md:w-5 md:h-5" />
          </a>
        ))}
      </div>

      {/* Chat Container */}
      <div className="flex flex-col w-full max-w-3xl h-[90vh] bg-white/90 backdrop-blur-sm rounded-xl shadow-xl border border-gray-200/70 overflow-hidden">
        {/* Header */}
        <div className="p-4 border-b border-gray-200 bg-white flex items-center gap-3">
          <div className="p-2 bg-blue-100 rounded-lg text-blue-600">
            <FaRobot className="w-5 h-5" />
          </div>
          <div>
            <h2 className="font-medium text-gray-800">AI Assistant</h2>
            <p className="text-xs text-gray-500">Powered by your API</p>
          </div>
        </div>
        
        {/* Messages area */}
        <div className="flex-1 overflow-y-auto px-4 md:px-6 py-4 space-y-3 scrollbar-thin scrollbar-thumb-gray-300/50 scrollbar-track-transparent">
          {messages.length === 0 && (
            <div className="h-full flex flex-col items-center justify-center text-gray-400">
              <div className="p-4 mb-3 bg-gray-100 rounded-full">
                <FaRobot className="w-8 h-8 text-gray-400" />
              </div>
              <p className="text-sm">How can I help you today?</p>
            </div>
          )}
          
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`p-3.5 rounded-lg max-w-[85%] leading-relaxed break-words transition-all duration-200
                ${
                  msg.role === "user"
                    ? "bg-blue-500/10 text-gray-800 self-end ml-auto border border-blue-500/20"
                    : "bg-gray-100/70 text-gray-800 self-start mr-auto border border-gray-200"
                }`}
            >
              {msg.text}
            </div>
          ))}

          {loading && (
            <div className="flex items-center justify-start space-x-1.5 py-2">
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-75"></div>
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-150"></div>
            </div>
          )}

          <div ref={chatEndRef} />
        </div>

        {/* Input area */}
        <div className="p-3 border-t border-gray-200/70 bg-white/80 backdrop-blur-sm">
          <div className={`flex items-center gap-2 bg-gray-100/50 rounded-lg px-3.5 py-2 transition-all duration-200
            ${loading ? 'opacity-80' : 'opacity-100'} focus-within:ring-2 focus-within:ring-blue-300/50 focus-within:bg-white`}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && !loading && sendMessage()}
              placeholder="Type a message..."
              className="flex-1 bg-transparent text-gray-800 placeholder-gray-400/70 text-sm focus:outline-none"
              spellCheck={false}
              disabled={loading}
            />
            <button
              onClick={sendMessage}
              disabled={loading || !input.trim()}
              className={`p-2 rounded-full transition-all duration-200 ${input.trim() ? 
                'bg-blue-500 hover:bg-blue-600 text-white shadow-sm hover:shadow-md' : 
                'bg-gray-300/50 text-gray-400 cursor-not-allowed'}`}
              aria-label="Send message"
            >
              <IoSend className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}