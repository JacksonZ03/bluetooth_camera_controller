# Bluetooth Sony Camera Controller
A tool to press the record button on the Sony camera using the Bluetooth protocol.

## Quickstart
Make sure bluetooth is enabled on your computer and on the camera.

### Windows
1. Make sure python 3.12+ is installed on your computer.
2. Install the requirements using `pip install -r requirements.txt`.
3. Run 
    ```
    python3 bluetooth-address-finder.py
    ``` 
    and note down the address of the camera.
4. Copy that address into the address variable in `camera-record.py`.
5. To start recording run:
    ```
    python3 camera-record.py
    ```

### Mac
1. Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```
2. Run: 
    ```
    python3 bluetooth-address-finder.py
    ``` 
    and note down the address of the camera.
3. Copy that address into the address variable in `camera-record.py`.
4. To start recording run:
    ```
    python3 camera-record.py
    ```


## Additional Information
If you want to compile the `camera-record.py` script into an executable, run 
```
pyinstaller camera-record.py --onefile
```
Since you only need the `camera-record` executable, feel free to delete the other garbage folders and files that are auto generated by PyInstaller during the build process.

Or you can run the `build-executable.sh` script to do the same thing automatically (for Mac users).

### (For Mac users specifically)
After running `build-executable.sh`, click `camera_record.command` whenever you want to start recording. 

This command file will automatically close the Terminal window afterwards whereas simply clicking the compiled `camera-record` executable will leave the Terminal window open afterwards (which is kind of annoying).

But since `camera_record.command` is just a optional wrapper for the `camera-record` executable, you don't have to use `camera_record.command` at all if you don't want to.