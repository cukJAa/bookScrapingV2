from scheduler.scheduler import startScheduler

if __name__ == "__main__":
    print("Starting the web scraping process...")
    print("If you want to stop the process, press Ctrl+C on the keyboard.")
    print("")
    try :
        print("Scheduler started successfully.")
        startScheduler()
    except KeyboardInterrupt:
        print("Scraping stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    