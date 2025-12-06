import axios from 'axios'

export async function getTasks(filters = {}) {
  const params = new URLSearchParams(filters).toString()
  const { data } = await axios.get(`/api/tasks/?${params}`)
  return data
}
