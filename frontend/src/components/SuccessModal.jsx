export default function SuccessModal({ onClose, tableId }) {
  return (
    <>
      <div style={{ position: 'fixed', inset: 0, background: 'rgba(45,25,10,0.6)', backdropFilter: 'blur(4px)', zIndex: 300, animation: 'fadeIn 0.3s ease' }} />
      <div style={{ position: 'fixed', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', background: '#FFFAF3', borderRadius: 24, padding: '44px 36px 36px', zIndex: 301, textAlign: 'center', maxWidth: 340, width: '90%', animation: 'scaleIn 0.4s cubic-bezier(0.34,1.56,0.64,1)', boxShadow: '0 24px 64px rgba(61,43,31,0.25)' }}>
        <div style={{ width: 80, height: 80, background: 'linear-gradient(135deg, #E8821A, #F5A623)', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 40, margin: '0 auto 20px', animation: 'successPop 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.1s both', boxShadow: '0 8px 24px rgba(232,130,26,0.35)' }}>✓</div>
        <h2 style={{ fontFamily: "'Playfair Display', serif", fontSize: 24, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 10 }}>Đặt Món Thành Công!</h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: 15, lineHeight: 1.6, marginBottom: 8 }}>Đơn hàng của bàn số <strong style={{ color: 'var(--amber)' }}>{tableId}</strong> đã được ghi nhận.</p>
        <p style={{ color: 'var(--text-muted)', fontSize: 13, marginBottom: 28 }}>Nhân viên sẽ phục vụ bạn trong giây lát 🙏</p>
        <div style={{ display: 'flex', justifyContent: 'center', gap: 6, marginBottom: 24 }}>
          {[0,1,2].map(i => <div key={i} style={{ width: 8, height: 8, borderRadius: '50%', background: i === 1 ? 'var(--amber)' : 'var(--amber-pale)', border: '1.5px solid var(--amber)' }} />)}
        </div>
        <button onClick={onClose} style={{ width: '100%', padding: '14px', background: 'linear-gradient(135deg, #3D2B1F, #5C3D28)', color: '#FFFAF3', border: 'none', borderRadius: 'var(--radius)', fontSize: 15, fontWeight: 600, cursor: 'pointer', boxShadow: '0 4px 16px rgba(61,43,31,0.3)' }}>
          Tiếp tục xem menu
        </button>
      </div>
    </>
  )
}