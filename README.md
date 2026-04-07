================================================================                
                      PROGRAM INSTRUCTIONS
================================================================

To execute the Python application, follow these steps within the 
VS Code environment:

1. Open the Terminal: 
   Navigate to the top menu and select Terminal > New Terminal 
   (or press Ctrl + `).

2. Verify Python Installation: 
   Ensure Python 3 is installed by typing: python --version

3. Run the Script: 
   Type the following command and press Enter: 
   python threading_demo.py

4. Observe Output: 
   The console will display timestamped log messages showing the 
   concurrent execution of both functions, followed by a final 
   message confirming the threads have completed their tasks.

----------------------------------------------------------------
THREAD MANAGEMENT
----------------------------------------------------------------

The application utilizes the built-in threading module to achieve 
concurrency. The management process follows a three-step lifecycle:

* Initialization: Two thread objects (thread1 and thread2) are 
  created using the Thread class. The target parameter points 
  each thread to a specific function (display_message_one and 
  display_message_two).

* Execution: The .start() method is called for both threads. 
  This transitions the threads from the "New" state to the 
  "Runnable" state, allowing the Python interpreter and the OS 
  to begin execution.

* Synchronization: The .join() method is implemented for both 
  threads. This ensures the "Main" thread pauses its execution 
  until both child threads have finished their tasks, preventing 
  the program from exiting prematurely.

----------------------------------------------------------------
OS CREATION AND THE THREAD CONTROL BLOCK (TCB)
----------------------------------------------------------------

When the start() method is called, the Python interpreter makes 
a system call to the Operating System to request the creation of 
a new thread. The OS manages this via the Thread Control Block 
(TCB)—a kernel data structure that acts as an "ID card" for the 
thread. 

The TCB holds vital information, including:
- Thread ID: A unique identifier for the OS to track the thread.
- Program Counter (PC): Tracks the current instruction.
- Register Set: Stores the thread’s current working data.
- Stack Pointer: Points to the private stack for local variables.
- Thread State: Tracks if the thread is Running, Ready, or Blocked.

Using the TCB, the OS performs context switching, allowing the 
CPU to switch between threads rapidly, creating the illusion of 
perfect parallelism.

----------------------------------------------------------------
DIFFICULTIES AND CHALLENGES
----------------------------------------------------------------

A primary challenge was maintaining organized console output. 
In multi-threaded environments, standard print() calls can 
"interleave" (overlap) if threads access the console 
simultaneously. 

To solve this, I implemented the 'logging' module, which is 
thread-safe. Additionally, the .join() method was critical to 
ensure the "completion" message only appeared after all 
background tasks were finalized.