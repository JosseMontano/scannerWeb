import { config } from "../config";

export const downloadFile = async (url: string, nameFile:string, data) => {
  try {
    const respuesta = await fetch(config.endpoint + url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

    if (!respuesta.ok) {
      throw new Error("Error al descargar el archivo");
    }

    const blob = await respuesta.blob();
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = nameFile;
    link.click();
  } catch (error) {
    console.error("Error:", error);
  }
};
