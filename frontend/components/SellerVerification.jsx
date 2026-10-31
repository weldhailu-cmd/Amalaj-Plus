import React, { useState } from 'react';

export default function SellerVerification() {
    const [platform, setPlatform] = useState('Telegram');
    const [channelName, setChannelName] = useState('');
    const [price, setPrice] = useState('');
    const [idFront, setIdFront] = useState(null);
    const [idBack, setIdBack] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        alert('National ID & First-Time Listing submitted securely. Verification in progress!');
    };

    return (
        <div className="max-w-3xl mx-auto px-6 py-8 bg-[#16203a] border border-slate-700/60 rounded-3xl shadow-2xl text-slate-100 space-y-6">
            <div className="border-b border-slate-800 pb-4">
                <span className="text-xs text-amber-400 font-bold uppercase tracking-wider">Anti-Scam Protection</span>
                <h2 className="text-2xl font-black text-white mt-1">One-Time Seller National ID Verification</h2>
                <p className="text-xs text-slate-400 mt-1">Required only for your first listing to ensure absolute marketplace trust.</p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6 text-xs">
                {/* Platform Selection */}
                <div className="space-y-2">
                    <label className="font-bold text-slate-300">Select Platform</label>
                    <div className="grid grid-cols-3 sm:grid-cols-5 gap-3">
                        {['Telegram', 'YouTube', 'TikTok', 'Instagram', 'Facebook'].map((p) => (
                            <button
                                type="button"
                                key={p}
                                onClick={() => setPlatform(p)}
                                className={`py-2 rounded-xl font-bold border transition ${platform === p ? 'bg-amber-500 text-slate-950 border-amber-400' : 'bg-slate-900 text-slate-300 border-slate-800'}`}
                            >
                                {p}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Channel Details */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="space-y-1">
                        <label className="font-bold text-slate-300">Channel / Account Name</label>
                        <input 
                            type="text" 
                            placeholder="e.g. Sportsphere" 
                            value={channelName}
                            onChange={(e) => setChannelName(e.target.value)}
                            className="w-full bg-slate-900 border border-slate-800 rounded-xl p-3 text-white focus:border-amber-500 outline-none"
                            required 
                        />
                    </div>
                    <div className="space-y-1">
                        <label className="font-bold text-slate-300">Asking Price (ETB)</label>
                        <input 
                            type="text" 
                            placeholder="e.g. 15000 ETB" 
                            value={price}
                            onChange={(e) => setPrice(e.target.value)}
                            className="w-full bg-slate-900 border border-slate-800 rounded-xl p-3 text-white focus:border-amber-500 outline-none"
                            required 
                        />
                    </div>
                </div>

                {/* National ID Upload Section */}
                <div className="bg-slate-900/80 border border-amber-500/30 rounded-2xl p-5 space-y-4">
                    <div className="flex items-center gap-2 text-amber-400 font-bold">
                        <i className="fa-solid fa-id-card"></i>
                        <span>National ID / Fayida Verification (First-Time Only)</span>
                    </div>
                    <p className="text-[11px] text-slate-400">Upload clear images of your official ID to prevent fraud and protect buyers.</p>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div className="space-y-1.5">
                            <label className="font-bold text-slate-300">ID Front Side *</label>
                            <input 
                                type="file" 
                                onChange={(e) => setIdFront(e.target.files[0])}
                                className="w-full text-slate-400 text-[10px] file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-amber-500 file:text-slate-950 hover:file:bg-amber-400 cursor-pointer"
                                required 
                            />
                        </div>
                        <div className="space-y-1.5">
                            <label className="font-bold text-slate-300">ID Back Side *</label>
                            <input 
                                type="file" 
                                onChange={(e) => setIdBack(e.target.files[0])}
                                className="w-full text-slate-400 text-[10px] file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-amber-500 file:text-slate-950 hover:file:bg-amber-400 cursor-pointer"
                                required 
                            />
                        </div>
                    </div>
                </div>

                {/* Submit Button */}
                <button 
                    type="submit" 
                    className="w-full py-3.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-black rounded-xl shadow-lg transition cursor-pointer text-sm"
                >
                    Submit Listing & Verify ID 🛡️
                </button>
            </form>
        </div>
    );
}