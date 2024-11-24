def run_turing_machine(input_tape):
    tape = input_tape + ['', '', '_']  # Menambahkan blank spaces di akhir
    head = 0
    current_state = 'q0'
    final_state = 'qf'
    
    transition_table = {
        ('q0', '1'): ('q0', '0', 'R'),
        ('q0', '0'): ('q0', '0', 'R'),
        ('q0', ''): ('qf', '', 'N'),
    }
    
    accepting_states = {'qf'}
    
    print(f"\nMenjalankan mesin dengan input: {''.join(input_tape)}")
    print("-" * 50)
    
    step = 0
    while current_state != final_state and step < 100:  # Menambahkan batas langkah untuk menghindari loop tak terbatas
        current_symbol = tape[head]
        
        print(f"Langkah {step}:")
        print(f"  Pita      : {''.join(tape)}")
        print(f"  Kepala baca: {' ' * head + '^'}")
        print(f"  Keadaan   : {current_state}")
        print(f"  Simbol    : {current_symbol}\n")
        
        if (current_state, current_symbol) in transition_table:
            new_state, new_symbol, direction = transition_table[(current_state, current_symbol)]
            
            tape[head] = new_symbol
            current_state = new_state
            
            if direction == 'R':
                head += 1
            elif direction == 'L':
                head -= 1
        else:
            print("Transisi tidak ditemukan!")
            print("\nStatus: DITOLAK (Rejected)")
            print("Alasan: Tidak ada transisi yang valid untuk kombinasi state dan simbol saat ini")
            return
        
        step += 1
    
    print("\nHasil Akhir:")
    print(f"Pita akhir: {''.join(tape)}")
    print(f"State akhir: {current_state}")
    
    if current_state in accepting_states:
        print("Status: DITERIMA (Accepted)")
        print("Alasan: Berhasil mencapai state akhir yang valid")
    else:
        print("Status: DITOLAK (Rejected)")
        print("Alasan: Tidak berhasil mencapai state akhir yang valid")

# Test Case 1: Input yang diterima (semua 1 dan 0)
print("\nTest Case 1 - Input Valid")
run_turing_machine(['1', '1', '0', '1'])

# Test Case 2: Input yang diterima (hanya 0)
print("\nTest Case 2 - Input Valid")
run_turing_machine(['0', '0', '0'])

# Test Case 3: Input yang ditolak (karakter tidak valid)
print("\nTest Case 3 - Input Invalid")
run_turing_machine(['1', '2', '0'])  # Mengandung '2' yang tidak ada dalam transisi

# Test Case 4: Input yang diterima (string kosong)
print("\nTest Case 4 - Input Valid")
run_turing_machine([])

# Test Case 5: Input yang ditolak (karakter khusus)
print("\nTest Case 5 - Input Invalid")
run_turing_machine(['1', '@', '0'])  # Mengandung '@' yang tidak ada dalam transisi