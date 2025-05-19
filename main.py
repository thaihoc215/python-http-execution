import httpx
import asyncio
import execute_api

async def main():
    # await execute_api.get_by_query_param()
    # await execute_api.post_body_json()
    # await execute_api.post_body_form_data()
    # await post_form_data_file()
    # await execute_api.post_form_data_file_using_param()
    # await execute_api.post_body_raw()
    # await execute_api.put_body_json()
    # await execute_api.delete_by_id()
    
    # await execute_api.get_with_basic_auth()
    await execute_api.get_with_basic_auth()
    await execute_api.get_secure_breeds()



if __name__ == "__main__":
    asyncio.run(main())
