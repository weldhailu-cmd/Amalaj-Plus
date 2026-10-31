import React, { useState, useEffect } from 'react';

export default function HowItWorks() {
    const steps = [
        { 
            badge: "Step 1 of 3", 
            title: "1. Disengaged Parties", 
            desc: "Buyer & Seller connect securely through our verified digital marketplace platform.", 
            img: "/static/step1-connection.png" 
        },
        { 
            badge: "Step 2 of 3", 
            title: "2. Escrow Protection", 
            desc: "Funds are deposited securely into Amalaj Plus escrow until asset transfer is verified.", 
            img: "/static/step2-escrow.png" 
        },
        { 
            badge: "Step 3 of 3", 
            title: "3. Unified Agreement", 
            desc: "Successful transfer confirmed and funds released safely to the seller.", 
            img: "/static/step3-agreement.png" 
        }
    ];

    const [currentStep, setCurrentStep] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentStep((prev) => (prev + 1) % steps.length);
        }, 4000);
        return () => clearInterval(interval);
    }, [steps.length]);

    const s = steps[currentStep];

    return (
        <section id="howItWorks" className="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
            <div className="text-center max-w-2xl mx-auto mb-8 space-y-2">
                <span className="text-xs text-amber-400 font-bold uppercase tracking-wider">Secure Escrow Workflow</span>
                <h2 className="text-3xl font-black text-white tracking-tight">How Amalaj Plus Works</h2>
                <p className="text-slate-400 text-xs">Safe, transparent, and verified digital asset trading & tool rentals in Ethiopia.</p>
            </div>

            <div className="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl max-w-4xl mx-auto text-center relative overflow-hidden">
                <div className="mb-6 flex justify-center">
                    <img 
                        src={s.img} 
                        alt="Step Illustration" 
                        className="max-h-64 object-contain rounded-xl shadow-lg border border-amber-500/20" 
                        onError={(e) => { e.target.src = 'https://via.placeholder.com/400x200?text=Amalaj+Plus+Escrow'; }} 
                    />
                </div>
                <div className="inline-block px-3 py-1 rounded-full bg-amber-500/20 text-amber-400 text-xs font-bold mb-2">
                    {s.badge}
                </div>
                <h3 className="text-2xl font-black text-white mb-2">{s.title}</h3>
                <p className="text-slate-300 text-sm max-w-xl mx-auto mb-6">{s.desc}</p>
                
                <div className="flex justify-center space-x-2">
                    {steps.map((_, idx) => (
                        <span 
                            key={idx} 
                            className={`w-3 h-3 rounded-full transition-all duration-300 ${idx === currentStep ? 'bg-amber-500' : 'bg-slate-700'}`}
                        ></span>
                    ))}
                </div>
            </div>
        </section>
    );
}