import React, { useState, useEffect } from 'react';

export default function Dashboard() {
    const [activeTab, setActiveTab] = useState('dashboard');
    const [listings, setListings] = useState([]);
    const [rentals, setRentals] = useState([]);

    useEffect(() => {
        // Load client listings from localStorage
        const storedListings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
        setListings(storedListings);
        
        // Mock active rentals
        setRentals([
            { id: 1, tool_name: 'UnlockTool Pro', status: 'ACTIVE', expires: '3 Hours Active' }
        ]);
    }, []);

    // Calculate dynamic analytics from user listings
    const totalChannels = listings.length + 14; // Base mock + user created
    const soldChannels = listings.filter(l => l.status === 'SOLD').length + 5;
    const pendingChannels = listings.filter(l => l.status !== 'SOLD').length + 4;
    const totalIncome = 24100; // Total earnings in ETB

    return (
        <div className="max-w-7xl mx-auto px-6 py-8 space-y-8 mb-16">
            {/* Top Header Welcome */}
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-[#16203a] border border-slate-700/60 rounded-3xl p-6 shadow-xl">
                <div>
                    <span className="text-xs text-amber-400 font-bold uppercase tracking-wider">Real-time account, activity & financial analytics</span>
                    <h1 className="text-2xl font-black text-white tracking-tight mt-1">Welcome back, ኃይለወልደ ኪዳን</h1>
                </div>
                <div className="flex items-center space-x-2 bg-slate-900 px-4 py-2 rounded-2xl border border-slate-800">
                    <i className="fa-solid fa-wallet text-amber-400"></i>
                    <span className="text-sm font-black text-white">3,500 ETB</span>
                </div>
            </div>

            {/* Navigation Tabs */}
            <div className="flex space-x-2 bg-[#16203a] p-1.5 rounded-2xl border border-slate-700/60 w-fit">
                <button 
                    onClick={() => setActiveTab('dashboard')} 
                    className={`px-5 py-2.5 rounded-xl transition cursor-pointer text-xs font-bold ${activeTab === 'dashboard' ? 'bg-amber-500 text-slate-950 shadow-lg' : 'text-slate-300 hover:text-white'}`}
                >
                    📊 Overview Analytics
                </button>
                <button 
                    onClick={() => setActiveTab('listings')} 
                    className={`px-5 py-2.5 rounded-xl transition cursor-pointer text-xs font-bold ${activeTab === 'listings' ? 'bg-amber-500 text-slate-950 shadow-lg' : 'text-slate-300 hover:text-white'}`}
                >
                    🛍️ My Listings ({listings.length})
                </button>
                <button 
                    onClick={() => setActiveTab('rentals')} 
                    className={`px-5 py-2.5 rounded-xl transition cursor-pointer text-xs font-bold ${activeTab === 'rentals' ? 'bg-amber-500 text-slate-950 shadow-lg' : 'text-slate-300 hover:text-white'}`}
                >
                    ⚡ Tool Rentals
                </button>
            </div>

            {/* Tab 1: Overview Dashboard & Analytics (Jano Market Style) */}
            {activeTab === 'dashboard' && (
                <div className="space-y-6">
                    {/* 4 Main Analytics Cards */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                        <div className="bg-[#16203a] border border-slate-700/60 rounded-2xl p-5 shadow-xl space-y-2 relative overflow-hidden">
                            <div className="flex justify-between items-center">
                                <span className="text-xs text-slate-400">Total Balance</span>
                                <span className="text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold">Live</span>
                            </div>
                            <div className="text-2xl font-black text-white">0 ETB</div>
                            <p className="text-[10px] text-slate-400">Available for withdrawal</p>
                        </div>

                        <div className="bg-[#16203a] border border-slate-700/60 rounded-2xl p-5 shadow-xl space-y-2 relative overflow-hidden">
                            <div className="flex justify-between items-center">
                                <span className="text-xs text-slate-400">Total Income</span>
                                <span className="text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold">Live</span>
                            </div>
                            <div className="text-2xl font-black text-amber-400">{totalIncome.toLocaleString()} ETB</div>
                            <p className="text-[10px] text-slate-400">Lifetime escrow earnings</p>
                        </div>

                        <div className="bg-[#16203a] border border-slate-700/60 rounded-2xl p-5 shadow-xl space-y-2 relative overflow-hidden">
                            <div className="flex justify-between items-center">
                                <span className="text-xs text-slate-400">Sold Channels</span>
                                <span className="text-[10px] bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded font-bold">Secured</span>
                            </div>
                            <div className="text-2xl font-black text-white">{soldChannels}</div>
                            <p className="text-[10px] text-slate-400">Successfully transferred</p>
                        </div>

                        <div className="bg-[#16203a] border border-slate-700/60 rounded-2xl p-5 shadow-xl space-y-2 relative overflow-hidden">
                            <div className="flex justify-between items-center">
                                <span className="text-xs text-slate-400">Total Channels</span>
                                <span className="text-[10px] bg-purple-500/20 text-purple-400 px-2 py-0.5 rounded font-bold">Active</span>
                            </div>
                            <div className="text-2xl font-black text-white">{totalChannels}</div>
                            <p className="text-[10px] text-slate-400">Managed in portfolio</p>
                        </div>
                    </div>

                    {/* Deposit Analytics Section */}
                    <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-6 shadow-xl space-y-4">
                        <div className="flex justify-between items-center border-b border-slate-800 pb-3">
                            <div>
                                <h3 className="font-bold text-white text-sm">Deposit Analytics</h3>
                                <p className="text-[11px] text-slate-400">Approved & processing deposits over the last 30 days</p>
                            </div>
                            <span className="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">🛡️ Escrow Verified</span>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                            <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 space-y-1">
                                <span className="text-slate-400">Approved Deposits</span>
                                <div className="text-lg font-black text-emerald-400">0 ETB</div>
                            </div>
                            <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 space-y-1">
                                <span className="text-slate-400">Processing (Pending)</span>
                                <div className="text-lg font-black text-amber-400">0 ETB</div>
                            </div>
                            <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 space-y-1">
                                <span className="text-slate-400">Rejected Deposits</span>
                                <div className="text-lg font-black text-red-400">0 ETB</div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Tab 2: My Listings */}
            {activeTab === 'listings' && (
                <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-6 shadow-xl space-y-4">
                    <div className="flex justify-between items-center mb-4">
                        <h3 className="font-bold text-white text-sm">Your Posted Digital Assets & Escrow Status</h3>
                        <span className="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">🛡️ Escrow Secured</span>
                    </div>
                    <div className="space-y-3">
                        {listings.length === 0 ? (
                            <div className="p-6 bg-slate-900/60 rounded-2xl border border-slate-800 text-xs text-slate-400 text-center space-y-2">
                                <p>No active listings found in your storage yet.</p>
                                <span className="text-amber-400 font-semibold block">Use the Post Asset form above to publish your first channel!</span>
                            </div>
                        ) : (
                            listings.map((l, index) => (
                                <div key={index} className="p-4 bg-slate-900/80 rounded-2xl border border-slate-800 flex justify-between items-center text-xs">
                                    <div>
                                        <span className="text-amber-400 font-bold">{l.platform}</span> - <strong className="text-white text-sm">{l.title}</strong>
                                        <p className="text-[11px] text-slate-400 mt-0.5">Subscribers/Views: {l.subCount} | Price: {l.price} ETB</p>
                                    </div>
                                    <span className="text-emerald-400 font-bold bg-emerald-500/10 px-3 py-1.5 rounded-full text-[10px]">Active & Generating</span>
                                </div>
                            ))
                        )}
                    </div>
                </div>
            )}

            {/* Tab 3: Tool Rentals */}
            {activeTab === 'rentals' && (
                <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-6 shadow-xl space-y-4">
                    <div className="flex justify-between items-center mb-4">
                        <h3 className="font-bold text-white text-sm">Your Active Tool Rentals</h3>
                        <span className="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">⚡ Remote Access Active</span>
                    </div>
                    <div className="space-y-3">
                        {rentals.map((r) => (
                            <div key={r.id} className="p-4 bg-slate-900/60 rounded-2xl border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
                                <div>
                                    <strong className="text-white text-sm">{r.tool_name}</strong>
                                    <p className="text-[11px] text-amber-400 mt-0.5">Duration Package: {r.expires}</p>
                                </div>
                                <span className="px-3 py-1.5 bg-emerald-500/10 text-emerald-400 rounded-full font-bold text-[10px]">Session Connected</span>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}