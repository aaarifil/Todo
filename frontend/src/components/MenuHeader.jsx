export default function MenuHeader({ tableId }) {
  return (
    <header style={{ background: 'linear-gradient(135deg, #3D2B1F 0%, #5C3D28 60%, #7A4E35 100%)', padding: '32px 24px 28px', textAlign: 'center', position: 'relative', overflow: 'hidden' }}>
      <div style={{ position: 'absolute', top: -40, right: -40, width: 160, height: 160, borderRadius: '50%', background: 'rgba(232,130,26,0.12)', pointerEvents: 'none' }} />
      <div style={{ position: 'absolute', bottom: -30, left: -30, width: 100, height: 100, borderRadius: '50%', background: 'rgba(245,166,35,0.08)', pointerEvents: 'none' }} />
      <div style={{ fontSize: 40, marginBottom: 8, animation: 'pulse 2.5s ease-in-out infinite' }}>🍜</div>
      <h1 style={{ fontFamily: "'Playfair Display', serif", fontSize: 'clamp(22px, 5vw, 32px)', fontWeight: 700, color: '#FFFAF3', letterSpacing: '0.02em', marginBottom: 6 }}>
        Thực Đơn Hôm Nay
      </h1>
      <div style={{ display: 'inline-flex', alignItems: 'center', gap: 8, background: 'rgba(232,130,26,0.25)', border: '1px solid rgba(232,130,26,0.4)', borderRadius: 100, padding: '5px 16px', marginTop: 4 }}>
        <span style={{ fontSize: 14 }}>🪑</span>
        <span style={{ color: '#F5C87A', fontSize: 13, fontWeight: 600, letterSpacing: '0.05em' }}>Bàn số {tableId}</span>
      </div>
      <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 20, overflow: 'hidden' }}>
        <svg viewBox="0 0 1200 20" preserveAspectRatio="none" style={{ width: '100%', height: '100%' }}>
          <path d="M0,10 C300,20 600,0 900,10 C1050,16 1150,8 1200,10 L1200,20 L0,20 Z" fill="#FFFAF3" />
        </svg>
      </div>
    </header>
  )
}