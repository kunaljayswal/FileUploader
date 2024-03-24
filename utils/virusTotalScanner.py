import aiohttp
import asyncio
import config

API_KEY = config.api_key
virus_total_api = 'https://www.virustotal.com/vtapi/v2/url/'

async def scan_file_url(file_url):
    url = virus_total_api + 'scan'
    params = {'apikey': API_KEY, 'url': file_url}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params) as response:
            return await response.json()

async def scan_result(resource):
    url = virus_total_api + 'report'
    params = {'apikey': API_KEY, 'resource': resource}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()

async def start_scan(file_to_scan):
    print("Scan request sending", file_to_scan)
    result = await scan_file_url(file_to_scan)
    print("Scan request sent", result)
    resource_id = result['resource']
    print("Scan result receiving in progress for resourceid", resource_id)

    await asyncio.sleep(15)
    
    result = await scan_result(resource_id)
    print("Scan result received", result)
    verbose_msg = result['verbose_msg']

    while verbose_msg == "Resource does not exist in the dataset" or not result['scans']:
        result = await scan_result(resource_id)
        print("Scan result received again", result)
        verbose_msg = result['verbose_msg']

        if verbose_msg != "Resource does not exist in the dataset" and result['scans']:
            break
        else:
            print("Resource not yet available, retrying in 10 seconds...")
            await asyncio.sleep(10)

    return result['scans']['Avira']['detected']