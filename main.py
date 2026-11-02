def main():
    from task_manager import TaskManager
    manager = TaskManager()

    while True:
        print('\n Gestor de tareas')
        print('=================')
        print()
        print('Opciones:')
        print('1. Añadir tarea')
        print('2. Listar tareas')
        print('3. Completar tarea')
        print('4. Eliminar tarea')
        print('5. Salir')
        print()
        choice = input("Seleccione una opción: ")

        match choice:
            case "1":
                description = input("Descripción de la tarea: ")
                manager.add_task(description)
            case "2":
                manager.list_tasks()
            case "3":
                task_id = int(input("ID de la tarea a completar: "))
                manager.complete_task(task_id)
            case "4":
                task_id = int(input("ID de la tarea a eliminar: "))
                manager.delete_task(task_id)
            case "5":
                print("Saliendo...")
                return
            case _:
                print("Opción no válida.")


if __name__ == "__main__":
    main()