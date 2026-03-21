import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import MenuPage from './pages/MenuPage.jsx'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/menu" element={<MenuPage />} />
        <Route path="*" element={<Navigate to="/menu?table=1" replace />} />
      </Routes>
    </BrowserRouter>
  )
}