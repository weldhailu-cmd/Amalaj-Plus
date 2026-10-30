import React, { useState } from 'react';

export default function PostAdForm() {
    const [title, setTitle] = useState('');
    const [link, setLink] = useState('');
    const [platform, setPlatform] = useState('Telegram');
    const [assetType, setAssetType] = useState('Channel');
    const [price, setPrice] = useState('');
    const [subCount, setSubCount] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!title || !link || !price) return;

        let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
        listings.push({
            platform: `${platform} (${assetType})`,
            title,
            price,
            subCount: subCount || 'Auto-scan verified',
            link,
            date: new Date().toLocaleDateString()
        });
        localStorage.setItem('amalaj_listings', JSON.stringify(listings));

        setTitle('');
        setLink('');
        setPrice('');
        setSubCount('');
        alert("Ad published successfully with Admin Escrow Protection! (2% fee applies)");
    };

    return (
        <div className="bg-[#1c2541] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-4 max-w-xl mx-auto text-xs">
            <div className="flex justify-between items-center pb-3 border-b border-slate-800">
                <h3 className="text-base font-bold text-white">Post Digital Asset Ad</h3>
                <span className="text-amber-400 font-bold">2% Escrow Protected</span>
            </div>
            <form onSubmit={handleSubmit} className="space-y-3">
                <div>
                    <label className="block text-slate-300 font-semibold mb-1">Asset Name / Title *</label>
                    <input 
                        type="text" 
                        value={title} 
                        onChange={(e) => setTitle(e.target.value)} 
                        required 
                        placeholder="e.g., Habesha Tech Channel" 
                        className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500"
                    />
                </div>
                <div>
                    <label className="block text-slate-300 font-semibold mb-1">Channel / Page Link * (Hidden from public)</label>
                    <input 
                        type="url" 
                        value={link} 
                        onChange={(e) => setLink(e.target.value)} 
                        required 
                        placeholder="https://t.me/your_channel" 
                        className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500"
                    />
                </div>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-slate-300 font-semibold mb-1">Platform *</label>
                        <select 
                            value={platform} 
                            onChange={(e) => setPlatform(e.target.value)} 
                            className="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500"
                        >
                            <option value="Telegram">Telegram</option>
                            <option value="TikTok">TikTok</option>
                            <option value="YouTube">YouTube</option>
                            <option value="Facebook">Facebook</option>
                        </select>
                    </div>
                    <div>
                        <label className="block text-slate-300 font-semibold mb-1">Asset Type *</label>
                        <select 
                            value={assetType} 
                            onChange={(e) => setAssetType(e.target.value)} 
                            className="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500"
                        >
                            <option value="Channel">Channel / Page</option>
                            <option value="Group">Group</option>
                            <option value="Bot">Bot</option>
                            <option value="Account">Account</option>
                        </select>
                    </div>
                </div>
                <div>
                    <label className="block text-slate-300 font-semibold mb-1">Full Page Screenshot Proof * (AI OCR Auto-Scan)</label>
                    <input 
                        type="file" 
                        accept="image/*" 
                        required 
                        className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-slate-400 text-[11px] focus:outline-none file:mr-3 file:py-1 file:px-3 file:rounded-lg file:border-0 file:text-xs file:font-bold file:bg-amber-500 file:text-slate-950 cursor-pointer"
                    />
                </div>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-slate-300 font-semibold mb-1">Subscribers / Followers</label>
                        <input 
                            type="number" 
                            value={subCount} 
                            onChange={(e) => setSubCount(e.target.value)} 
                            placeholder="Auto-filled via OCR" 
                            className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500"
                        />
                    </div>
                    <div>
                        <label className="block text-slate-300 font-semibold mb-1">Asking Price (ETB) *</label>
                        <input 
                            type="number" 
                            value={price} 
                            onChange={(e) => setPrice(e.target.value)} 
                            required 
                            placeholder="5000" 
                            className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500"
                        />
                    </div>
                </div>
                <button type="submit" className="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer">
                    Publish Ad with Escrow Protection &rarr;
                </button>
            </form>
        </div>
    );
}