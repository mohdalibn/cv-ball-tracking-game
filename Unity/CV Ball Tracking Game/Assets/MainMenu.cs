using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{

    [SerializeField] RectTransform fader;

    private void Start()
    {

        // ALPHA/OPACITY ANIMATION
        fader.gameObject.SetActive(true);
        LeanTween.alpha(fader, 1, 0);
        LeanTween.alpha(fader, 0, 0.5f).setOnComplete(() =>{
            fader.gameObject.SetActive(false);
        });

        // SCALE ANIMATION
        // fader.gameObject.SetActive(true);
        // LeanTween.scale(fader, new Vector3(1, 1, 1), 0);
        // LeanTween.scale(fader, Vector3.zero, 0.5f).setEase(LeanTweenType.easeInOutQuad).setOnComplete(() =>{
        //     fader.gameObject.SetActive(false);
        // });
    }

    // This method will be called wheneve the play button is pressed. Use the the "using UnityEngine.SceneMangement;"
    public void PlayGame()
    {
        fader.gameObject.SetActive(true);

        // ALPHA/OPACITY ANIMATION
        LeanTween.alpha(fader, 0, 0);
        LeanTween.alpha(fader, 1, 0.5f).setOnComplete(() =>{
            SceneManager.LoadScene("CV Ball Tracking Game");
        });


        // SCALE ANIMATION
        // LeanTween.scale(fader, Vector3.zero, 0f);
        // LeanTween.scale(fader, new Vector3(1, 1, 1), 0.5f).setEase(LeanTweenType.easeInOutQuad).setOnComplete(() => {
        //     SceneManager.LoadScene("CV Ball Tracking Game");
        // });
        
    }

    // This method will be called when the Quit button is pressed in the main menu
    public void QuitGame()
    {
        Application.Quit();
    }

}
