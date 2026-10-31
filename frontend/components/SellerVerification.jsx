import React, { useState } from 'react';

export default function SellerVerification() {
    const [platform, setPlatform] = useState('Telegram');
    const [channelName, setChannelName] = useState('');
    const [price, setPrice] = useState('');
    const [idFront, setIdFront] = useState(null);
    const [idBack, setIdBack] = useState(null);
    const [portrait, setPortrait] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        alert('Verification & Listing submitted successfully! Admin will review your ID and channel stats.');
    };

    return (
        <div className="max-w-3xl mx-auto px-6 py-8 bg-[#16203a] border border-slate-700/60 rounded-3xl shadow-2xl text-slate-100 space-y-6">
            <div className="border-b border-slate-800 pb-4">
                <span className="text-xs text-amber-400 font-bold uppercase tracking-wider">Security & Anti-Scam Verification</span>
                <h2 className="text-2xl font-black text-white mt-1">Seller Identity & Channel Listing</h2>
                <p className="text-xs text-slate-400 mt-1">To protect buyers, every seller must provide official ID verification before posting an ad.</p>
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
                        <label className="font-bold text-slate-300">Channel / Account Title</label>
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

                {/* Mandatory ID Verification Section */}
                <div className="bg-slate-900/80 border border-amber-500/30 rounded-2xl p-5 space-y-4">
                    <div className="flex items-center gap-2 text-amber-400 font-bold">
                        <i className="fa-solid fa-shield-halved"></i>
                        <span>Mandatory Seller ID Verification (Fayida / National ID / Passport)</span>
                    </div>
                    <p className="text-[11px] text-slate-400">Please upload high-quality scanned images of your legal identification card.</p>

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

                    {/* Optional Portrait Photo */}
                    <div className="space-y-1.5 pt-2 border-t border-slate-800">
                        <label className="font-bold text-slate-300">Seller Portrait / Guard Photo (Optional)</label>
                        <input 
                            type="file" 
                            onChange={(e) => setPortrait(e.target.files[0])}
                            className="w-full text-slate-400 text-[10px] file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-slate-800 file:text-slate-200 hover:file:bg-slate-700 cursor-pointer"
                        />
                        <span className="text-[10px] text-slate-500 block">Helps build extra trust with verified buyers.</span>
                    </div>
                </div>

                {/* Submit Button */}
                <button 
                    type="submit" 
                    className="w-full py-3.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-black rounded-xl shadow-lg transition cursor-pointer text-sm"
                >
                    Verify & Submit Channel Listing 🛡️
                </button>
            </form>
        </div>
    );
}