import React, { useState, useEffect } from 'react';

export default function ToolRental() {
    const [tools, setTools] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedTool, setSelectedTool] = useState(null);
    const [anydeskId, setAnydeskId] = useState('');
    const [telegram, setTelegram] = useState('');
    const [paymentMethod, setPaymentMethod] = useState('Chapa');
    const [receiptFile, setReceiptFile] = useState(null);

    useEffect(() => {
        fetchTools();
    }, []);

    const fetchTools = async () => {
        try {
            const res = await fetch('/api/v1/tools');
            const data = await res.json();
            setTools(data);
        } catch (err) {
            console.error("Failed to load tools", err);
        }
    };

    const openModal = (tool) => {
        setSelectedTool(tool);
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setSelectedTool(null);
        setAnydeskId('');
        setTelegram('');
        setReceiptFile(null);
    };

    const handleRentSubmit = async (e) => {
        e.preventDefault();
        if (!selectedTool) return;

        const formData = new FormData();
        formData.append('tool_id', selectedTool.id);
        formData.append('renter_anydesk_id', anydeskId);
        formData.append('renter_telegram', telegram);
        formData.append('payment_method', paymentMethod);
        if (receiptFile) {
            formData.append('receipt_file', receiptFile);
        }

        try {
            const res = await fetch('/api/v1/tools/rent', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (data.success) {
                alert(data.message);
                closeModal();
                fetchTools();
            } else {
                alert(data.detail || "Rental process failed.");
            }
        } catch (err) {
            console.error(err);
            alert("Connection error during rental.");
        }
    };

    return (
        <section id="toolRentalSection" className="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
            <div className="flex justify-between items-center mb-8">
                <div>
                    <span className="text-xs text-amber-400 font-bold uppercase tracking-wider">For Technicians</span>
                    <h2 className="text-2xl font-black text-white tracking-tight mt-1">Mobile Repair Software Tool Rentals ⚡</h2>
                    <p className="text-slate-400 text-xs mt-1">Rent professional flashing software tools instantly.</p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {tools.map((t) => (
                    <div key={t.id} className="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl flex flex-col justify-between">
                        <div className="space-y-2">
                            <div className="flex justify-between items-center">
                                <h3 className="font-bold text-white text-base">{t.tool_name}</h3>
                                <span className="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB {t.rental_price} / {t.rental_duration}</span>
                            </div>
                            <p className="text-xs text-slate-300">{t.description}</p>
                            <p className="text-[11px] text-amber-300 font-semibold"><i class="fa-solid fa-link"></i> {t.connection_type}</p>
                        </div>
                        <button 
                            onClick={() => openModal(t)} 
                            disabled={t.status !== 'AVAILABLE'}
                            className={`w-full py-2 font-bold rounded-xl text-xs transition cursor-pointer ${t.status === 'AVAILABLE' ? 'bg-amber-500 hover:bg-amber-400 text-slate-950' : 'bg-slate-700 text-slate-400 cursor-not-allowed'}`}
                        >
                            {t.status === 'AVAILABLE' ? 'Rent Tool Now ⚡' : 'Currently Rented (Busy)'}
                        </button>
                    </div>
                ))}
            </div>

            {/* Rental Modal */}
            {isModalOpen && selectedTool && (
                <div className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4">
                    <div className="bg-[#1c2541] border border-slate-700 rounded-3xl p-6 max-w-md w-full space-y-4 shadow-2xl text-xs">
                        <div className="flex justify-between items-center pb-2 border-b border-slate-800">
                            <h3 className="font-bold text-white text-sm">Rent Tool: {selectedTool.tool_name}</h3>
                            <button onClick={closeModal} className="text-slate-400 hover:text-white cursor-pointer"><i class="fa-solid fa-xmark text-base"></i></button>
                        </div>
                        <form onSubmit={handleRentSubmit} className="space-y-3">
                            <div>
                                <label className="block text-slate-300 font-semibold mb-1">Your AnyDesk ID / Remote ID *</label>
                                <input 
                                    type="text" 
                                    value={anydeskId} 
                                    onChange={(e) => setAnydeskId(e.target.value)} 
                                    required 
                                    placeholder="e.g., 1 234 567 890" 
                                    className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500" 
                                />
                            </div>
                            <div>
                                <label className="block text-slate-300 font-semibold mb-1">Telegram Username *</label>
                                <input 
                                    type="text" 
                                    value={telegram} 
                                    onChange={(e) => setTelegram(e.target.value)} 
                                    required 
                                    placeholder="e.g., @myusername" 
                                    className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500" 
                                />
                            </div>
                            <div>
                                <label className="block text-slate-300 font-semibold mb-1">Payment Method *</label>
                                <select 
                                    value={paymentMethod} 
                                    onChange={(e) => setPaymentMethod(e.target.value)} 
                                    className="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500"
                                >
                                    <option value="Chapa">Chapa Payment Gateway (Instant)</option>
                                    <option value="Bank Transfer">Bank Transfer Receipt (Manual)</option>
                                </select>
                            </div>
                            {paymentMethod === 'Bank Transfer' && (
                                <div>
                                    <label className="block text-slate-300 font-semibold mb-1">Upload Receipt *</label>
                                    <input 
                                        type="file" 
                                        accept="image/*" 
                                        onChange={(e) => setReceiptFile(e.target.files[0])} 
                                        className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-slate-400 text-[11px] cursor-pointer" 
                                    />
                                </div>
                            )}
                            <button type="submit" className="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer shadow-md">
                                Proceed to Secure Payment & Start Timer &rarr;
                            </button>
                        </form>
                    </div>
                </div>
            )}
        </section>
    );
}