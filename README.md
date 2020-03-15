# Send-SMS Github Actions  
> When a push occurs in the master branch, a SMS is sent to the user.  

![slack-message](https://user-images.githubusercontent.com/18473861/76513573-da17fb00-6499-11ea-8358-437f003959fd.png)  

## Parameters
Make sure that these parameters are required as [Github Secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)
| Parameter | Type | Description |
|-----------|------|-------------|
| `MOBILE_NO` | `string` | Your mobile no |
| `AWS_KEY_ID` | `string` | Your aws key id |
| `AWS_KEY_ACCESS` | `string` | Your aws access key |


## Usage

```yaml
name: When a push occurs in the master branch, a sms is sent to the user.
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: notify
        id: notify
        
        uses: vbhv007/send-sms-action@master
        with:
          mobile_no: ${{ secrets.MOBILE_NO }}
          aws_key_id: ${{ secrets.AWS_KEY_ID }}
          aws_key_access: ${{ secrets.AWS_KEY_ACCESS }}
      
      - name : Run
        run: |
          echo 'Run!'
```
