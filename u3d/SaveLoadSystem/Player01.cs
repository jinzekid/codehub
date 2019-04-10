using UnityEngine;

[System.Serializable]
public class Player01 : GameData
{
    // 只能保存
    // string, bool, float, int[]
    // 如果需要保存 Vector3 -> float[3], Color -> float[3]
    // 需要序列化的属性
    public int level = 3;
    public int health = 40;
    public int[] position;
    public bool hasHair = true;
    public float height = 1.75f;

    // 不需要序列化属性
    [System.NonSerialized]
    public bool sex;
}
