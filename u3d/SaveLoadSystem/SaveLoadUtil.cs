using UnityEngine;

public class SaveLoadUtil : MonoBehaviour
{ 
    // 保存数据
    public void SaveData()
    {
        Player01 player = new Player01() { level = 10, health = 150, sex = true };
        SaveSystem.SaveGameData(player, "player.fun");
    }

    // 加载数据
    public void LoadData()
    {
        Player01 player = SaveSystem.LoadGameData("player.fun") as Player01;
        Debug.Log("player level:" + player.level + ", health:" + player.health + ",sex:" + player.sex);
    }
}
