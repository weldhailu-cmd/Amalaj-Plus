import React, { useState } from 'react';

export default function MarketplaceListings() {
    const [selectedPlatform, setSelectedPlatform] = useState('ALL');

    const [listings, setListings] = useState([
        { id: 1, platform: 'Telegram', title: 'Crypto Hub', price: '15,000 ETB', subscribers: '12K', views: '45K' },
        { id: 2, platform: 'YouTube', title: 'Sportsphere', price: '78,000 ETB', subscribers: '303K', views: '14M' },
        { id: 3, platform: 'TikTok', title: 'Habesha Trends', price: '6,500 ETB', subscribers: '45K', views: '1.2M' },
        { id: 4, platform: 'Instagram', title: 'thela.stone291', price: '910 ETB', subscribers: '1.1K', views: '1 Avg' },
        { id: 5, platform: 'Facebook', title: 'Osama Jami', price: '1,950 ETB', subscribers: '5.1K', views: '12 Likes' }
    ]);

    const filteredListings = selectedPlatform === 'ALL' 
        ? listings 
        : listings.filter(item => item.platform === selectedPlatform);

    return (
        <div className="max-w-7xl mx-auto px-6 py-8 space-y-8">
            {/* Platform Selection Cards */}
            <div className="space-y-4">
                <div className="flex justify-between items-center">
                    <h2 className="text-base font-black text-white">Select Platform to Browse Listings</h2>
                    <span className="text-xs text-amber-400 font-bold">Verified Channels & Accounts</span>
                </div>

                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
                    <div onClick={() => setSelectedPlatform('ALL')} className="bg-[#16203a] border-2 border-amber-500 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl transition transform hover:-translate-y-1">
                        <div className="w-10 h-10 mx-auto rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400 font-bold"><i className="fa-solid fa-layer-group"></i></div>
                        <div className="font-black text-white text-xs">All Platforms</div>
                        <span className="inline-block px-2 py-0.5 bg-amber-500 text-slate-950 text-[10px] font-bold rounded-full">Browse Listings</span>
                    </div>

                    <div onClick={() => setSelectedPlatform('Telegram')} className="bg-[#16203a] border border-blue-500/40 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl transition transform hover:-translate-y-1">
                        <div className="w-10 h-10 mx-auto rounded-xl bg-blue-500/20 flex items-center justify-center text-blue-400 font-bold"><i className="fa-brands fa-telegram"></i></div>
                        <div className="font-black text-white text-xs">Telegram</div>
                        <span className="inline-block px-2 py-0.5 bg-blue-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                    </div>

                    <div onClick={() => setSelectedPlatform('YouTube')} className="bg-[#16203a] border border-red-500/40 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl transition transform hover:-translate-y-1">
                        <div className="w-10 h-10 mx-auto rounded-xl bg-red-500/20 flex items-center justify-center text-red-500 font-bold"><i className="fa-brands fa-youtube"></i></div>
                        <div className="font-black text-white text-xs">YouTube</div>
                        <span className="inline-block px-2 py-0.5 bg-red-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                    </div>

                    <div onClick={() => setSelectedPlatform('TikTok')} className="bg-[#16203a] border border-pink-500/40 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl transition transform hover:-translate-y-1">
                        <div className="w-10 h-10 mx-auto rounded-xl bg-pink-500/20 flex items-center justify-center text-pink-400 font-bold"><i className="fa-brands fa-tiktok"></i></div>
                        <div className="font-black text-white text-xs">TikTok</div>
                        <span className="inline-block px-2 py-0.5 bg-pink-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                    </div>

                    <div onClick={() => setSelectedPlatform('Instagram')} className="bg-[#16203a] border border-purple-500/40 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl transition transform hover:-translate-y-1">
                        <div className="w-10 h-10 mx-auto rounded-xl bg-gradient-to-tr from-amber-500 via-pink-600 to-purple-600 flex items-center justify-center text-white font-bold"><i className="fa-brands fa-instagram"></i></div>
                        <div className="font-black text-white text-xs">Instagram</div>
                        <span className="inline-block px-2 py-0.5 bg-purple-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                    </div>

                    <div onClick={() => setSelectedPlatform('Facebook')} className="bg-[#16203a] border border-blue-600/40 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl transition transform hover:-translate-y-1">
                        <div className="w-10 h-10 mx-auto rounded-xl bg-blue-600/20 flex items-center justify-center text-blue-500 font-bold"><i className="fa-brands fa-facebook"></i></div>
                        <div className="font-black text-white text-xs">Facebook</div>
                        <span className="inline-block px-2 py-0.5 bg-blue-700 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                    </div>
                </div>
            </div>

            {/* Filtered Listings Grid */}
            <div className="space-y-4">
                <div className="flex justify-between items-center bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                    <div>
                        <span className="text-xs text-amber-400 font-bold uppercase tracking-wider">{selectedPlatform} Active</span>
                        <h2 className="text-xl font-black text-white mt-1">Verified Marketplace Listings</h2>
                    </div>
                    <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-full text-xs font-bold">Protected by 2% Escrow</span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    {filteredListings.map((item) => (
                        <div key={item.id} className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-5 shadow-xl space-y-3 text-xs">
                            <span className="px-2 py-0.5 bg-blue-600 text-white rounded font-bold text-[9px] uppercase">{item.platform}</span>
                            <h3 className="font-bold text-white text-sm">{item.title}</h3>
                            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-2.5 flex justify-between text-[11px]">
                                <div><strong className="text-white">{item.subscribers}</strong><div className="text-slate-400 text-[9px]">Subscribers</div></div>
                                <div><strong className="text-white">{item.views}</strong><div className="text-slate-400 text-[9px]">Views/Likes</div></div>
                            </div>
                            <div className="flex justify-between items-center pt-2 border-t border-slate-800">
                                <div><div className="text-[9px] text-slate-400 uppercase">Price</div><div className="text-base font-black text-amber-400">{item.price}</div></div>
                                <button onClick={() => alert(`Initiating Escrow Purchase for ${item.title}`)} className="px-3.5 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl cursor-pointer shadow">Buy Now</button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}