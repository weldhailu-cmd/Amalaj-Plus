import React, { useState, useEffect } from 'react';

export default function EscrowTimer({ channelName, price, platform }) {
    // 3 Days Protection Period Countdown (Mocked to 49 mins 37 secs for visual display)
    const [timeLeft, setTimeLeft] = useState({
        days: 0,
        hours: 0,
        mins: 49,
        secs: 37
    });

    useEffect(() => {
        const timer = setInterval(() => {
            setTimeLeft(prev => {
                if (prev.secs > 0) {
                    return { ...prev, secs: prev.secs - 1 };
                } else if (prev.mins > 0) {
                    return { ...prev, mins: prev.mins - 1, secs: 59 };
                } else if (prev.hours > 0) {
                    return { ...prev, hours: prev.hours - 1, mins: 59, secs: 59 };
                } else if (prev.days > 0) {
                    return { ...prev, days: prev.days - 1, hours: 23, mins: 59, secs: 59 };
                }
                return prev;
            });
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    return (
        <div className="max-w-4xl mx-auto px-6 py-8 space-y-6">
            {/* Top Asset Header */}
            <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-6 shadow-xl flex items-center justify-between">
                <div className="flex items-center space-x-4">
                    <div className="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-xl font-black">
                        🛡️
                    </div>
                    <div>
                        <span className="text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded font-bold uppercase">{platform || 'TikTok'}</span>
                        <h2 className="text-lg font-black text-white mt-1">{channelName || 'orthodox sebket'}</h2>
                    </div>
                </div>
                <div className="text-right">
                    <div className="text-xl font-black text-emerald-400">{price || '3,500'} ETB</div>
                    <p className="text-[10px] text-slate-400">SELLING • Processing</p>
                </div>
            </div>

            {/* Protection Period Countdown Card */}
            <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl space-y-6 text-center">
                <div className="space-y-1">
                    <span className="text-xs text-amber-400 font-bold uppercase tracking-wider flex items-center justify-center gap-1.5">
                        <i className="fa-solid fa-shield-halved"></i> Protection Period
                    </span>
                    <h3 className="text-2xl font-black text-white">Protection Period Countdown</h3>
                    <p className="text-xs text-slate-400 max-w-lg mx-auto">
                        Funds stay frozen until this timer ends (3 days window). If the previous owner reclaims access, report to admin with screenshots before time runs out.
                    </p>
                </div>

                {/* 4 Counter Boxes */}
                <div className="grid grid-cols-4 gap-3 max-w-xl mx-auto">
                    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-inner">
                        <div className="text-2xl md:text-3xl font-black text-white">{String(timeLeft.days).padStart(2, '0')}</div>
                        <div className="text-[10px] text-slate-400 uppercase tracking-wider mt-1">Days</div>
                    </div>
                    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-inner">
                        <div className="text-2xl md:text-3xl font-black text-white">{String(timeLeft.hours).padStart(2, '0')}</div>
                        <div className="text-[10px] text-slate-400 uppercase tracking-wider mt-1">Hours</div>
                    </div>
                    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-inner">
                        <div className="text-2xl md:text-3xl font-black text-amber-400">{String(timeLeft.mins).padStart(2, '0')}</div>
                        <div className="text-[10px] text-slate-400 uppercase tracking-wider mt-1">Mins</div>
                    </div>
                    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-inner">
                        <div className="text-2xl md:text-3xl font-black text-amber-400">{String(timeLeft.secs).padStart(2, '0')}</div>
                        <div className="text-[10px] text-slate-400 uppercase tracking-wider mt-1">Secs</div>
                    </div>
                </div>

                {/* Order Summary & Actions */}
                <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 text-left space-y-3 max-w-xl mx-auto text-xs">
                    <div className="flex justify-between border-b border-slate-800 pb-2">
                        <span className="text-slate-400">Your payout</span>
                        <span className="font-bold text-white">3,500 ETB</span>
                    </div>
                    <div className="flex justify-between border-b border-slate-800 pb-2">
                        <span className="text-slate-400">Order ID</span>
                        <span className="font-mono text-amber-400">1c677a93-5af...</span>
                    </div>
                    <div className="flex justify-between">
                        <span className="text-slate-400">Platform</span>
                        <span className="font-bold text-white">TikTok</span>
                    </div>
                </div>

                <button 
                    onClick={() => alert("Opening secure admin-mediated chat...")} 
                    className="w-full max-w-xl py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl transition cursor-pointer text-xs shadow-lg flex items-center justify-center gap-2"
                >
                    <i className="fa-solid fa-comments"></i> Open Chat with Admin & Buyer
                </button>
            </div>
        </div>
    );
}