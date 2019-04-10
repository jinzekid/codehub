using UnityEngine;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

public static class SaveSystem
{
    public static string GetDataPath(string name)
    {
        string path = Application.persistentDataPath + "/" + name;
        return path;
    }

    public static void SaveGameData(GameData data, string pathName)
    {
        Debug.Log("1111");
        BinaryFormatter formatter = new BinaryFormatter();
        string path = GetDataPath(pathName);

        FileStream stream = new FileStream(path, FileMode.Create);

        formatter.Serialize(stream, data);
        stream.Close();
        Debug.Log("SaveSystem:>>SaveGameData success:" + pathName);
    }

    public static GameData LoadGameData(string pathName)
    {
        string path = GetDataPath(pathName);
        Debug.Log("SaveSystem:>>LoadGameData:" + pathName);

        if (File.Exists(path))
        {
            BinaryFormatter formatter = new BinaryFormatter();
            FileStream stream = new FileStream(path, FileMode.Open);

            GameData data = formatter.Deserialize(stream) as GameData;
            stream.Close();

            return data;
        }
        else
        {
            Debug.LogError("File not found in " + path);
            return null;
        }

    }
}
