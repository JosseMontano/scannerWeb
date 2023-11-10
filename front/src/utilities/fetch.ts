import { config } from "../config";

export async function fetchData(url: string) {
  try {
    const response = await fetch(config.endpoint + url);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error.message);
  }
}
