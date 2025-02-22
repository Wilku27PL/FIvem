#!/usr/bin/env python
try:
    from lupa import LuaRuntime, LuaError
except ImportError as e:
    print(f"Failed to import LuaRuntime: {e}")
    exit(1)

import traceback
import os

def main():
    try:
        lua = LuaRuntime(unpack_returned_tuples=True)
        
        lua_file_path = os.path.join(os.path.dirname(__file__), 'aim_assist.lua')
        if not os.path.exists(lua_file_path):
            raise FileNotFoundError(f"The file 'aim_assist.lua' was not found at {lua_file_path}.")
        
        with open(lua_file_path, 'r') as file:
            lua_code = file.read()
        
        print("Lua code to be executed:")
        print(lua_code)
        
        try:
            lua.execute(lua_code)
            print("Executed Lua code from aim_assist.lua.")
            print("Notification: Lua code executed successfully.")
        except LuaError as e:
            print(f"A Lua error occurred: {e}")
            traceback.print_exc()
        except Exception as e:
            print(f"An unexpected error occurred during Lua execution: {e}")
            traceback.print_exc()
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__": 
    main()
    while True:
        try:
            input("Press Enter to exit...")  # Prevent the launcher from closing immediately
            break
        except EOFError:
            pass