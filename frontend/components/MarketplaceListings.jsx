import React, { useState } from 'react';

export default function MarketplaceListings() {
    // Sample mockup listings based on your design references (YouTube, Instagram, Facebook)
    const [listings, setListings] = useState([
        {
            id: 1,
            platform: 'YouTube',
            title: 'Sportsphere',
            category: 'Sports',
            price: '78,000 ETB',
            subscribers: '303K',
            views: '14M',
            status: 'ACTIVE',
            monetized: true,
            image: 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=100&h=100&fit=crop'
        },
        {
            id: 2,
            platform: 'YouTube',
            title: 'NextGoal',
            category: 'Entertainment',
            price: '14,950 ETB',
            subscribers: '33K',
            views: '3.3M',
            status: 'ACTIVE',
            monetized: false,
            image: 'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=100&h=100&fit=crop'
        },
        {
            id: 3,
            platform: 'Instagram',
            title: 'thela.stone291',
            category: 'Lifestyle',
            price: '910 ETB',
            subscribers: '1.1K',
            views: '1 Avg Likes',
            status: 'ACTIVE',
            monetized: false,
            image: 'https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=100&h=100&fit=crop'
        },
        {
            id: 4,
            platform: 'Facebook',
            title: 'Osama Jami',
            category: 'Business',
            price: '1,950 ETB',
            subscribers: '5.1K',
            views: '12 Page Likes',
            status: 'ACTIVE',
            monetized: false,
            image: 'https://images.unsplash.com/photo-1561948955-570b270e7c36?w=100&h=100&fit=crop'
        }
    ]);

    const handleBuy = (title, price) => {
        alert(`Initiating Escrow Purchase for ${title} (${price}). 2% escrow fee applies. Please proceed to deposit funds securely.`);
    };

    const handleChat = (title) => {
        alert(`Opening Secure Admin-Mediated Chat for ${title}. (Note: Sharing phone numbers or external links is auto-blocked by anti-scam guard).`);
    };

    return (
        <div className="max-w-7xl mx-auto px-6 py-8">
            <div className="mb-6 flex justify-between items-center">
                <div>
                    <h2 className="text-2xl font-black text-white tracking-tight">Browse Verified Marketplace Listings</h2>
                    <p className="text-slate-400 text-xs mt-1">All transactions are protected by 2% admin-gated escrow.</p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {listings.map((item) => {
                    // Dynamic styling based on platform
                    let brandBg = 'bg-red-600';
                    if (item.platform === 'Instagram') brandBg = 'bg-gradient-to-b from-purple-600 via-pink-600 to-amber-500';
                    if (item.platform === 'Facebook') brandBg = 'bg-blue-600';

                    return (
                        <div key={item.id} className="bg-[#16203a] border border-slate-700/60 rounded-3xl overflow-hidden shadow-2xl flex relative">
                            {/* Left Vertical Platform Badge Strip */}
                            <div className={`${brandBg} w-10 flex items-center justify-center py-6 shrink-0`}>
                                <span className="text-white font-bold text-xs tracking-widest uppercase transform -rotate-90 whitespace-nowrap">
                                    {item.platform}
                                </span>
                            </div>

                            {/* Main Card Content */}
                            <div className="p-5 flex-grow space-y-4">
                                {/* Top Row: Avatar, Title, Details Button */}
                                <div className="flex items-start justify-between">
                                    <div className="flex items-center space-x-3">
                                        <img src={item.image} alt={item.title} className="w-12 h-12 rounded-2xl object-cover border border-slate-700" />
                                        <div>
                                            <div className="flex items-center space-x-2">
                                                <span className="px-2 py-0.5 bg-blue-600 text-white rounded text-[10px] font-bold">NEW</span>
                                                <h3 className="font-bold text-white text-sm">{item.title}</h3>
                                            </div>
                                            <span className="text-[11px] text-slate-400 flex items-center gap-1 mt-0.5">
                                                <i className="fa-solid fa-globe"></i> Open on {item.platform}
                                            </span>
                                        </div>
                                    </div>
                                    <button onclick="alert('Opening Full Asset Detail View...')" className="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold border border-slate-700 transition cursor-pointer">
                                        Details
                                    </button>
                                </div>

                                {/* Tags */}
                                <div className="flex items-center space-x-2 text-[11px]">
                                    <span className="px-2.5 py-1 bg-slate-900 text-slate-300 rounded-lg border border-slate-800">{item.category}</span>
                                    <span className="px-2.5 py-1 bg-emerald-500/10 text-emerald-400 rounded-lg border border-emerald-500/20 font-semibold">Very Good Price</span>
                                </div>

                                {/* Stats Box */}
                                <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-3 flex justify-between items-center text-xs">
                                    <div className="flex items-center space-x-2">
                                        <i className="fa-solid fa-users text-slate-400"></i>
                                        <div>
                                            <div className="font-extrabold text-white">{item.subscribers}</div>
                                            <div className="text-[10px] text-slate-400">Subscribers</div>
                                        </div>
                                    </div>
                                    <div className="flex items-center space-x-2">
                                        <i className="fa-solid fa-eye text-slate-400"></i>
                                        <div>
                                            <div className="font-extrabold text-white">{item.views}</div>
                                            <div className="text-[10px] text-slate-400">Total Views</div>
                                        </div>
                                    </div>
                                    <div className="flex items-center space-x-1 px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full text-[10px] font-bold">
                                        <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse"></span>
                                        <span>{item.status}</span>
                                    </div>
                                </div>

                                {/* Price & Action Buttons (Buy + Chat) */}
                                <div className="flex items-center justify-between pt-2 border-t border-slate-800">
                                    <div>
                                        <div className="text-[10px] text-slate-400 uppercase tracking-wider">Price</div>
                                        <div className="text-lg font-black text-white">{item.price}</div>
                                    </div>
                                    <div className="flex space-x-2">
                                        <button 
                                            onClick={() => handleChat(item.title)}
                                            className="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer flex items-center gap-1"
                                            title="Secure Admin Chat"
                                        >
                                            <i class="fa-solid fa-comments"></i> Chat
                                        </button>
                                        <button 
                                            onClick={() => handleBuy(item.title, item.price)}
                                            className="px-4 py-2 bg-red-600 hover:bg-red-500 text-white font-bold rounded-xl text-xs transition cursor-pointer shadow-lg flex items-center gap-1.5"
                                        >
                                            <i class="fa-solid fa-cart-shopping"></i> Buy
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}