import React, { useState } from 'react';

export default function PostAdForm({ selectedPlatform = 'Telegram', onSubmit }) {
    const [platform, setPlatform] = useState(selectedPlatform);
    const [formData, setFormData] = useState({
        channelName: '',
        channelUrl: '',
        category: '',
        followers: '',
        description: '',
        price: '',
        telegramUsername: '',
        phoneNumber: '',
        monetized: false,
        screenshot: null
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: type === 'checkbox' ? checked : value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (onSubmit) {
            onSubmit({ platform, ...formData });
        }
    };

    return (
        <div className="modal-box bg-[#16203a] border border-amber-500/40 rounded-2xl p-6 text-white max-w-xl mx-auto">
            <div className="border-b border-slate-800 pb-3 mb-4 flex justify-between items-center">
                <div>
                    <span className="text-[10px] text-amber-400 font-bold uppercase tracking-wider">Step 2: Post Channel Listing</span>
                    <h2 className="text-lg font-black mt-1">Publish {platform} Asset</h2>
                </div>
                <span className="px-3 py-1 bg-emerald-500/10 text-emerald-400 rounded-full text-[10px] font-bold">
                    3-Day Escrow Protection
                </span>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4 text-xs">
                {/* Platform Selector Tabs */}
                <div>
                    <label className="block font-bold text-slate-300 mb-2">Select Platform</label>
                    <div className="grid grid-cols-5 gap-2">
                        {['Telegram', 'YouTube', 'TikTok', 'Instagram', 'Facebook'].map((p) => (
                            <button
                                type="button"
                                key={p}
                                onClick={() => setPlatform(p)}
                                className={`py-2 px-1 rounded-xl font-bold text-[10px] transition text-center border ${
                                    platform === p 
                                        ? 'bg-amber-500 text-slate-950 border-amber-400' 
                                        : 'bg-[#090d16] text-slate-400 border-slate-800 hover:border-slate-600'
                                }`}
                            >
                                {p}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Dashboard Screenshot Upload */}
                <div className="bg-[#090d16]/60 border border-dashed border-amber-500/30 rounded-2xl p-4">
                    <label className="block font-bold text-amber-400 mb-1 text-[11px]">
                        <i className="fa-solid fa-camera mr-1"></i> Dashboard Screenshot *
                    </label>
                    <p className="text-[10px] text-slate-400 mb-2">Upload a screenshot showing your logo, followers, and views. Do not crop.</p>
                    <input type="file" className="text-[10px] text-slate-400 w-full" required />
                </div>

                <div className="grid grid-cols-2 gap-3">
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Channel / Account Link *</label>
                        <input 
                            type="text" 
                            name="channelUrl"
                            placeholder="https://t.me/... or URL" 
                            value={formData.channelUrl}
                            onChange={handleChange}
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Category *</label>
                        <select 
                            name="category"
                            value={formData.category}
                            onChange={handleChange}
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500"
                            required
                        >
                            <option value="">Select category</option>
                            <option value="Crypto">Crypto & Finance</option>
                            <option value="Education">Education & Tech</option>
                            <option value="Entertainment">Entertainment</option>
                            <option value="Business">Business & E-commerce</option>
                        </select>
                    </div>
                </div>

                <div className="grid grid-cols-2 gap-3">
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Followers / Subscribers *</label>
                        <input 
                            type="number" 
                            name="followers"
                            placeholder="e.g. 50000" 
                            value={formData.followers}
                            onChange={handleChange}
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Asking Price (ETB) *</label>
                        <input 
                            type="number" 
                            name="price"
                            placeholder="e.g. 15000" 
                            value={formData.price}
                            onChange={handleChange}
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                </div>

                {/* Conditional YouTube Monetization Field */}
                {platform === 'YouTube' && (
                    <div className="bg-[#090d16] border border-slate-800 rounded-xl p-3 flex items-center justify-between">
                        <span className="font-bold text-slate-300">Monetization Status</span>
                        <label className="flex items-center gap-2 cursor-pointer">
                            <input 
                                type="checkbox" 
                                name="monetized"
                                checked={formData.monetized}
                                onChange={handleChange}
                                className="accent-amber-500 w-4 h-4"
                            />
                            <span className="text-amber-400 font-bold">Monetized Channel</span>
                        </label>
                    </div>
                )}

                <div>
                    <label className="block font-bold text-slate-300 mb-1">Description *</label>
                    <textarea 
                        name="description"
                        rows="2"
                        placeholder="Describe your channel details..." 
                        value={formData.description}
                        onChange={handleChange}
                        className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500"
                        required
                    ></textarea>
                </div>

                <div className="border-t border-slate-800 pt-3">
                    <div className="grid grid-cols-2 gap-3">
                        <div>
                            <label className="block font-bold text-slate-300 mb-1">Telegram Username *</label>
                            <input 
                                type="text" 
                                name="telegramUsername"
                                placeholder="@username" 
                                value={formData.telegramUsername}
                                onChange={handleChange}
                                className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                                required 
                            />
                        </div>
                        <div>
                            <label className="block font-bold text-slate-300 mb-1">Phone Number (+251) *</label>
                            <input 
                                type="tel" 
                                name="phoneNumber"
                                placeholder="+251..." 
                                value={formData.phoneNumber}
                                onChange={handleChange}
                                className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                                required 
                            />
                        </div>
                    </div>
                </div>

                {/* Seller Agreement Notice with 3-Day Escrow */}
                <div className="text-[10px] text-slate-400 bg-amber-500/5 border border-amber-500/20 p-3 rounded-xl">
                    <span className="font-bold text-amber-400">Escrow & Recovery Notice:</span> Payout to seller is released after a mandatory **3-day buyer recovery/escrow hold period** to guarantee total platform security.
                </div>

                <button 
                    type="submit" 
                    className="w-full py-3 bg-gradient-to-r from-emerald-500 to-emerald-400 text-slate-950 font-black rounded-xl cursor-pointer shadow-lg hover:brightness-110 transition mt-2"
                >
                    Publish Channel Ad 🚀
                </button>
            </form>
        </div>
    );
}