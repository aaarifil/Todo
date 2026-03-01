const apiBase = '/api/v1'

async function listTodos(){
  const q = document.getElementById('q').value || ''
  const is_done = document.getElementById('is_done').value
  const params = new URLSearchParams()
  if(q) params.append('q', q)
  if(is_done !== '') params.append('is_done', is_done)
  const res = await fetch(`${apiBase}/todos?`+params.toString())
  const data = await res.json()
  renderTodos(data.items)
}

function renderTodos(items){
  const ul = document.getElementById('todos')
  ul.innerHTML = ''
  if(!items.length) { ul.innerHTML = '<li>No todos</li>'; return }
  items.forEach(it => {
    const li = document.createElement('li')
    li.className = 'todo'
    li.innerHTML = `
      <div>
        <strong>${escapeHtml(it.title)}</strong>
        <div class="meta">${it.description||''} — ${new Date(it.created_at).toLocaleString()}</div>
      </div>
      <div class="actions">
        <button data-id="${it.id}" class="toggle">${it.is_done? 'Undo':'Done'}</button>
        <button data-id="${it.id}" class="delete">Delete</button>
      </div>
    `
    ul.appendChild(li)
  })
}

function escapeHtml(s){ return (s||'').replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"})[c]) }

document.getElementById('create-form').addEventListener('submit', async (e)=>{
  e.preventDefault()
  const title = document.getElementById('title').value
  const description = document.getElementById('description').value
  const res = await fetch(`${apiBase}/todos`, {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify({title, description})})
  if(res.ok){ document.getElementById('title').value=''; document.getElementById('description').value=''; listTodos() }
  else { alert('Error creating todo') }
})

document.getElementById('reload').addEventListener('click', (e)=>{ e.preventDefault(); listTodos() })

document.getElementById('todos').addEventListener('click', async (e)=>{
  const id = e.target.dataset.id
  if(!id) return
  if(e.target.classList.contains('delete')){
    if(!confirm('Delete?')) return
    const res = await fetch(`${apiBase}/todos/${id}`, {method:'DELETE'})
    if(res.ok) listTodos()
  }
  if(e.target.classList.contains('toggle')){
    // fetch current, then patch
    const getRes = await fetch(`${apiBase}/todos/${id}`)
    if(!getRes.ok) return alert('Not found')
    const todo = await getRes.json()
    const res = await fetch(`${apiBase}/todos/${id}`, {method:'PATCH', headers:{'content-type':'application/json'}, body: JSON.stringify({is_done: !todo.is_done})})
    if(res.ok) listTodos()
  }
})

// initial load
listTodos()
