import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_message_one() -> None:
    """
    Function for the first thread.
    Displays a text message including the function name.
    """
    logging.info("Hello from thread 1! Now executing the function: display_message_one")

def display_message_two() -> None:
    """
    Function for the second thread.
    Displays a text message including the function name.
    """
    logging.info("Hello from thread 2! Now executing the function: display_message_two")

def main() -> None:
    """
    Main function to create and manage threads.
    It initializes two threads, starts them, and waits for their completion.
    """
    # Create thread objects pointing to the target functions
    thread1 = threading.Thread(target=display_message_one)
    thread2 = threading.Thread(target=display_message_two)

    try:
        # Start the execution of the threads
        thread1.start()
        thread2.start()

        # Wait for both threads to complete before finishing the main program
        thread1.join()
        thread2.join()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Both threads have completed their tasks.")

if __name__ == "__main__":
    main()
