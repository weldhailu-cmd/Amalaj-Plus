import React, { useState } from 'react';

export default function SellerVerification({ onVerified }) {
    const [formData, setFormData] = useState({
        fatherName: '',
        motherName: '',
        phone: '',
        fayidaNum: '',
        idFront: null,
        idBack: null
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        // Validation and verification logic
        if (onVerified) {
            onVerified(formData.phone);
        }
    };

    return (
        <div className="modal-box bg-[#16203a] border border-amber-500/40 rounded-2xl p-6 text-white max-w-lg mx-auto">
            <div className="border-b border-slate-800 pb-3 mb-4">
                <span className="text-[10px] text-amber-400 font-bold uppercase tracking-wider">Step 1: Identity Verification</span>
                <h2 className="text-lg font-black mt-1">One-Time Seller National ID Verification</h2>
                <p className="text-xs text-slate-400 mt-1">Enter your details once. Existing sellers bypass automatically.</p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4 text-xs">
                <div className="grid grid-cols-2 gap-3">
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Father's Full Name (የአባት ስም)</label>
                        <input 
                            type="text" 
                            placeholder="Enter father's name" 
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Mother's Full Name (የእናት ስም)</label>
                        <input 
                            type="text" 
                            placeholder="Enter mother's name" 
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Phone Number (የስልክ ቁጥር)</label>
                        <input 
                            type="tel" 
                            id="sellerPhone" 
                            placeholder="09... / 07..." 
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                    <div>
                        <label className="block font-bold text-slate-300 mb-1">Fayida ID (16 Digits)</label>
                        <input 
                            type="text" 
                            maxLength="16" 
                            placeholder="16-digit Fayida number" 
                            className="w-full bg-[#090d16] border border-slate-800 rounded-xl p-2.5 text-white outline-none focus:border-amber-500" 
                            required 
                        />
                    </div>
                </div>

                {/* ID Photo Upload Box */}
                <div className="bg-[#090d16]/60 border border-dashed border-amber-500/30 rounded-2xl p-4 mt-2">
                    <div className="flex items-center gap-2 text-amber-400 font-bold text-xs mb-3">
                        <i className="fa-solid fa-id-card"></i>
                        <span>National ID / Fayida Photo Verification</span>
                    </div>
                    <div className="grid grid-cols-2 gap-3">
                        <div>
                            <label className="block font-bold text-slate-300 mb-1 text-[11px]">ID Front Side *</label>
                            <input type="file" className="text-[10px] text-slate-400 w-full" required />
                        </div>
                        <div>
                            <label className="block font-bold text-slate-300 mb-1 text-[11px]">ID Back Side *</label>
                            <input type="file" className="text-[10px] text-slate-400 w-full" required />
                        </div>
                    </div>
                </div>

                <button 
                    type="submit" 
                    className="w-full py-3 bg-gradient-to-r from-amber-500 to-amber-400 text-slate-950 font-black rounded-xl cursor-pointer shadow-lg hover:brightness-110 transition mt-4"
                >
                    Verify Identity & Continue 🛡️
                </button>
            </form>
        </div>
    );
}