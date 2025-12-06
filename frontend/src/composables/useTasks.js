import { ref, watch } from 'vue'
import { getTasks } from '@/api/taskService'

export function useTasks() {
  const tasks = ref([])
  const filters = ref({ status: '', search: '' })
  const loading = ref(false)

  const fetchTasks = async () => {
    loading.value = true
    tasks.value = await getTasks(filters.value)
    loading.value = false
  }

  // Atualiza automaticamente quando filtros mudam
  watch(filters, fetchTasks, { deep: true })

  return { tasks, filters, loading, fetchTasks }
}
