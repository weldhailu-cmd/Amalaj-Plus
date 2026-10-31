import React, { useState } from 'react';

export default function AdminChat() {
    const [messages, setMessages] = useState([
        { sender: 'Admin', text: 'Aregelh?', time: '02:17 PM', type: 'admin' },
        { sender: 'Buyer', text: 'Eyarekut new', time: '02:23 PM', type: 'buyer' },
        { sender: 'Admin', text: 'Data eyastekakelku new blual tnsh entebkew', time: '02:23 PM', type: 'admin' }
    ]);
    const [inputMsg, setInputMsg] = useState('');
    const [isCompleted, setIsCompleted] = useState(false);

    const handleSendMessage = (e) => {
        e.preventDefault();
        if (!inputMsg.trim() || isCompleted) return;

        setMessages([...messages, {
            sender: 'You (Admin)',
            text: inputMsg,
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
            type: 'you'
        }]);
        setInputMsg('');
    };

    const handleMarkComplete = () => {
        setIsCompleted(true);
        alert("Transaction marked as Complete! Escrow funds released, and chat is now securely locked.");
    };

    return (
        <div className="max-w-4xl mx-auto px-6 py-8">
            <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-4">
                {/* Chat Header */}
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 pb-4 border-b border-slate-800">
                    <div className="flex items-center space-x-3">
                        <div className="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold">
                            🛡️
                        </div>
                        <div>
                            <div className="flex items-center space-x-2">
                                <h3 className="font-bold text-white text-sm">orthodox sebket</h3>
                                <span className="text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded font-bold">TikTok</span>
                            </div>
                            <p className="text-[11px] text-slate-400">Selling • 3,500 ETB • <span className={isCompleted ? "text-emerald-400 font-bold" : "text-amber-400 font-bold"}>{isCompleted ? "Completed & Locked" : "Processing"}</span></p>
                        </div>
                    </div>

                    {/* Mark as Complete Button (Jano Market Style) */}
                    <button 
                        onClick={handleMarkComplete}
                        disabled={isCompleted}
                        className={`px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 shadow-lg ${isCompleted ? 'bg-emerald-500/20 text-emerald-400 cursor-not-allowed border border-emerald-500/30' : 'bg-emerald-600 hover:bg-emerald-500 text-white cursor-pointer'}`}
                    >
                        <i className="fa-solid fa-check-circle"></i>
                        {isCompleted ? 'Completed & Locked 🔒' : 'Mark as Complete'}
                    </button>
                </div>

                {/* Messages Box */}
                <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 h-80 overflow-y-auto space-y-3">
                    {messages.map((m, idx) => (
                        <div key={idx} className={`flex flex-col ${m.type === 'you' ? 'items-end' : 'items-start'}`}>
                            <div className="text-[10px] text-slate-400 mb-1 px-1">{m.sender} • {m.time}</div>
                            <div className={`p-3 rounded-2xl text-xs max-w-md ${m.type === 'you' ? 'bg-amber-500 text-slate-950 font-medium' : 'bg-slate-800 text-slate-200 border border-slate-700'}`}>
                                {m.text}
                            </div>
                        </div>
                    ))}
                    {isCompleted && (
                        <div className="p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-2xl text-center text-xs text-emerald-400 font-bold">
                            🔒 This transaction has been marked as complete. Chat is locked by admin escrow protection.
                        </div>
                    )}
                </div>

                {/* Chat Input Bar */}
                <form onSubmit={handleSendMessage} className="flex gap-2">
                    <input 
                        type="text" 
                        value={inputMsg}
                        onChange={(e) => setInputMsg(e.target.value)}
                        disabled={isCompleted}
                        placeholder={isCompleted ? "Chat is locked after completion." : "Type message to buyer, seller & admin..."}
                        className="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-500 disabled:opacity-50"
                    />
                    <button 
                        type="submit" 
                        disabled={isCompleted}
                        className="px-5 py-2.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl transition text-xs disabled:opacity-50 cursor-pointer shadow"
                    >
                        Send
                    </button>
                </form>
            </div>
        </div>
    );
}