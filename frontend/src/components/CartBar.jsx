export default function CartBar({ totalItems, totalPrice, onClick }) {
  return (
    <div style={{ position: 'fixed', bottom: 0, left: 0, right: 0, padding: '12px 16px', background: 'linear-gradient(to top, rgba(255,250,243,1) 70%, rgba(255,250,243,0))', zIndex: 100, animation: 'slideUp 0.35s ease' }}>
      <div style={{ maxWidth: 600, margin: '0 auto' }}>
        <button onClick={onClick} style={{ width: '100%', padding: '16px 24px', background: 'linear-gradient(135deg, #3D2B1F, #5C3D28)', color: '#FFFAF3', border: 'none', borderRadius: 'var(--radius)', fontSize: 15, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'space-between', boxShadow: '0 8px 32px rgba(61,43,31,0.35)' }}>
          <div style={{ background: 'var(--amber)', borderRadius: 100, minWidth: 28, height: 28, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 13, fontWeight: 700 }}>{totalItems}</div>
          <span style={{ flex: 1, textAlign: 'center', fontSize: 15 }}>🛒 Xem giỏ hàng</span>
          <span style={{ color: 'var(--amber-light)', fontWeight: 700 }}>{totalPrice.toLocaleString('vi-VN')}₫</span>
        </button>
      </div>
    </div>
  )
}