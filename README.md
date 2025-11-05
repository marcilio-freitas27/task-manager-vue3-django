### Task Manager with Vue and Django frameworks

```css

backend/
├── core/
│   ├── models/
│   │   └── task.py
│   ├── repositories/
│   │   └── task_repository.py
│   ├── services/
│   │   └── task_service.py
│   ├── serializers/
│   │   └── task_serializer.py
│   └── __init__.py
└── api/
    ├── views/
    │   └── task_view.py
    ├── urls.py
    └── __init__.py
```

```css
frontend/
├── src/
│   ├── api/
│   │   └── taskService.js
│   ├── composables/
│   │   └── useTasks.js
│   ├── views/
│   │   └── TaskListView.vue
│   ├── components/
│   │   └── TaskFilters.vue
│   ├── App.vue
│   └── main.js
```