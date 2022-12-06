class post_machine:
    '''
    Класс машина Поста post_machine

    Методы:
        ----------------------------------------------------------------------
        __init__(self, state, write_head, tape_list)
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - имитация ленты

        Назначение - автоматически вызываемый при создании каждого экземпляра метод
        ----------------------------------------------------------------------
        get_state(self)

        Назначение - метод возврата состояния
        ----------------------------------------------------------------------
        get_write_head(self)

        Назначение - метод возврата положения пишущей головки
        ----------------------------------------------------------------------
        get_tape_list(self)

        Назначение - метод возврата ленты
        ----------------------------------------------------------------------
        get_command_list(self)

        Назначение - метод возврата списка комманд
        ----------------------------------------------------------------------
        update_state(self, current_command, state, write_head, tape_list)
            current_command:
                type list
                Список - текущая команда
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - эмитация ленты

        Назначение - проверка возможности выполнения команды
        ----------------------------------------------------------------------
    '''

    ##################################################################################################
    def __init__(self, state, write_head, tape_list, command_list):
        '''
        __init__(self, state, write_head, tape_list)
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - имитация ленты
            command_list
                type list
                Список - список команд

        Назначение - автоматически вызываемый при создании каждого экземпляра метод
        '''
        self.state = state
        self.write_head = write_head
        self.tape_list = tape_list
        self.command_list = command_list
        self.first = True


    def get_state(self):
        '''
        get_state(self)

        Назначение - метод возврата состояния
        '''
        return self.state

    def get_write_head(self):
        '''
        get_write_head(self)

        Назначение - метод возврата положения пишущей головки
        '''
        return self.write_head

    def get_tape_list(self):
        '''
        get_tape_list(self)

        Назначение - метод возврата ленты
        '''
        return self.tape_list

    def get_command_list(self):
        '''
        get_command_list(self)

        Назначение - метод возврата списка комманд
        '''
        return self.command_list

    def update_state(self, current_command):
        '''
        update_state(self, current_command, state, write_head, tape_list)
            current_command:
                type list
                Список - текущая команда
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - имитация ленты

        Назначение - проверка возможности выполнения команды

        Логика работы:
        Анализируем возможность выполнить команду пользователя, проверяя ее на возможные ошибки
        Невозможно выполнить команду если она удовлетворяет следующим критериям
        1) при постановке метки, т.к. в используемой ячейке УЖЕ содержится метка
        2) при стирании метки, т.к. в используемой ячейке НЕ содержится метка
        '''
        if self.tape_list[self.write_head] == 1 and current_command[1] == 'v':
            print(f"Команда {current_command[0]} не может быть выполнена, т.к. в используемой ячейке УЖЕ содержится метка")
            return not self.state
        elif self.tape_list[self.write_head] == 0 and current_command[1] == '-':
            print(f"Команда {current_command[0]} не может быть выполнена, т.к. в используемой ячейке НЕ содержится метка")
            return not self.state
        else:
            return self.state

    ##################################################################################################
    """def task_teg(self, write_head, tape_list, next):
        tape_list[write_head] = 1
        return next
    def task_delete(self, write_head, tape_list, next):
        tape_list[write_head] = 0
        return next
    def task_go_right(self, write_head, tape_list, next):
        if write_head == len(tape_list) - 1:
            tape_list += [0] * 33
        write_head += 1
        return next
    def task_go_left(self, write_head, tape_list, next):
        if write_head == 0:
            tape_list[:0] = [0] * 33
            write_head = 33
        write_head -= 1
        return next
    def task_branching(self, write_head, tape_list, next):
        if tape_list[write_head]:
            pass

    def post_machine_work(self, current_command, state, write_head, tape_list, command_list, i = 0):
        '''
        '''
        current_command=command_list[i]

        if self.update_state(current_command, state, write_head, tape_list):
            current = current_command[0]
            task = current_command[1]
            next = current_command[2]

            if task == 'v':
                self.task_teg(write_head, tape_list, next)

            elif task == '-':
                self.task_delete(write_head, tape_list)

            elif task == '>':
                self.task_go_right(write_head, tape_list)

            elif task == '<':
                self.task_go_left(write_head, tape_list)

            elif task[0] == '?':
                self.task_branching(write_head, tape_list)

        elif not self.update_state(current_command, state, write_head, tape_list):
            return "Программа окончила свое выполнение"""

    def post_machine_working(self, i=0):

        if self.first:
            print('----------------------')
            print("Начальное состояние ленты")
            print(self.tape_list)
            print('----------------------')
            self.first = False
        else:
            print('----------------------')
            #print(f"Комманда {i}")
            print(self.tape_list)
            print('----------------------')

        current_command = self.command_list[i]
        can_work = self.update_state(current_command)

        task = current_command[1]

        if can_work:
            if task == 'stop':
                print("Программа окончила свое выполнение")
                return None
            elif task == 'v':
                self.tape_list[self.write_head] = 1
                i = current_command[2] - 1
            elif task == '-':
                self.tape_list[self.write_head] = 0
                i = current_command[2] - 1
            elif task == '>':
                if self.write_head == len(self.tape_list) - 1:
                    self.tape_list += [0] * 32
                self.write_head += 1
                i = current_command[2] - 1
            elif task == '<':
                if self.write_head == 0:
                    self.tape_list[:0] = [0] * 32
                    self.write_head += 32
                self.write_head -= 1
                i = current_command[2] - 1
            elif task == '?':
                if self.tape_list[self.write_head] == 1:
                    i = current_command[2][0] - 1
                else:
                    i = current_command[2][1] - 1
            self.post_machine_working(i)
        else:
            print("Программа окончила свое выполнение в связи с некоректной командой")
            return None



