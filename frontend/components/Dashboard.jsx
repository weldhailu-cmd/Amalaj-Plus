import React, { useState, useEffect } from 'react';

export default function Dashboard() {
    const [activeTab, setActiveTab] = useState('listings');
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

    return (
        <section id="dashboardSection" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800 mb-16">
            <div class="flex justify-between items-center mb-6">
                <div>
                    <h2 class="text-2xl font-black text-white tracking-tight">User Dashboard</h2>
                    <p class="text-slate-400 text-xs mt-1">Manage your active listings, view counts, and software tool rentals.</p>
                </div>
                <div class="flex space-x-2 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs font-semibold">
                    <button 
                        onClick={() => setActiveTab('listings')} 
                        class={`px-4 py-2 rounded-lg transition cursor-pointer ${activeTab === 'listings' ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-300 hover:text-white'}`}
                    >
                        My Listings
                    </button>
                    <button 
                        onClick={() => setActiveTab('rentals')} 
                        class={`px-4 py-2 rounded-lg transition cursor-pointer ${activeTab === 'rentals' ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-300 hover:text-white'}`}
                    >
                        My Rentals
                    </button>
                </div>
            </div>

            {activeTab === 'listings' ? (
                <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl space-y-4">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-white text-sm">Your Posted Digital Assets & Earnings</h3>
                        <span class="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">🛡️ Escrow Secured</span>
                    </div>
                    <div class="space-y-3">
                        {listings.length === 0 ? (
                            <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center">
                                <span>No active listings yet. Use the Post Asset form above!</span>
                                <span class="text-emerald-400 font-semibold">Escrow Ready</span>
                            </div>
                        ) : (
                            listings.map((l, index) => (
                                <div key={index} class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                                    <div>
                                        <span class="text-amber-400 font-bold">{l.platform}</span> - <strong class="text-white">{l.title}</strong>
                                        <p class="text-[10px] text-slate-400">Views Tracked: {l.subCount} | Price: {l.price} ETB</p>
                                    </div>
                                    <span class="text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-1 rounded-full text-[10px]">Active & Generating</span>
                                </div>
                            ))
                        )}
                    </div>
                </div>
            ) : (
                <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl space-y-4">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-white text-sm">Your Active Tool Rentals</h3>
                        <span class="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">⚡ Remote Access Active</span>
                    </div>
                    <div class="space-y-3">
                        {rentals.map((r) => (
                            <div key={r.id} class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
                                <div>
                                    <strong class="text-white">{r.tool_name}</strong>
                                    <p class="text-[10px] text-amber-400 mt-0.5">Duration Package: {r.expires}</p>
                                </div>
                                <span class="px-2.5 py-1 bg-emerald-500/10 text-emerald-400 rounded-full font-bold text-[10px]">Session Connected</span>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </section>
    );
}