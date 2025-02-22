from lupa import LuaRuntime, LuaError
import traceback

def main():
    try:
        lua = LuaRuntime(unpack_returned_tuples=True)
        
        with open('c:/Users/krysi/Desktop/FIvem/aim_assist.lua', 'r') as file:
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
    except FileNotFoundError:
        print("The file 'aim_assist.lua' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")  # Prevent the launcher from closing immediately