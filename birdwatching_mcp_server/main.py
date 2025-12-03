from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP("birdwatching_mcp_server", json_response=True)
GALLERY_URL = os.environ.get('GALLERY_URL')
USER_AGENT = "birdwatching_app/1.0"

@mcp.tool()
def get_gallery() -> dict:
    """
    Returns a list of photos and locations from the Birdwatching Flask app.

    Returns:
        dict with key “pictures”, list with {picture, location}
    """
    try:
        response = requests.get(GALLERY_URL)
        response.raise_for_status() 
        data = response.json()
        return {"status": "success", "pictures": data.get("pictures", [])}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
