<template>
  <div class="p-4">
    <h2 class="mb-3 text-xl font-bold">Minhas Tarefas</h2>

    <TaskFilters :filters="filters" />

    <DataTable :value="task" :loading="loading" paginator :rows="5">
      <Column field="title" header="Título" />
      <Column field="status" header="Status" />
      <Column field="created_at" header="Criada em" />
    </DataTable>
  </div>
</template>

<script setup>
import { DataTable, Column } from 'primevue'
import TaskFilters from '@/components/TaskFilters.vue'
import { useTasks } from '@/composables/useTasks'
import { ref, watch } from 'vue'

const task = ref([{
  id: 1,
  title: 'Tarefa de exemplo',
  status: 'Pendente',
  created_at: '2024-01-01'
}])

const { tasks, filters, loading, fetchTasks } = useTasks()
fetchTasks() // busca inicial
</script>
