# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CtMusic(models.Model):
    musicidx = models.AutoField(
        db_column="MusicIdx", primary_key=True
    )  # Field name made lowercase.
    groupidx = models.IntegerField(db_column="GroupIdx")  # Field name made lowercase.
    musiccode = models.CharField(
        db_column="MusicCode", max_length=16
    )  # Field name made lowercase.
    memidx = models.IntegerField(db_column="MemIdx")  # Field name made lowercase.
    cateidx = models.IntegerField(db_column="CateIdx")  # Field name made lowercase.
    musictitle = models.CharField(
        db_column="MusicTitle", max_length=300
    )  # Field name made lowercase.
    musictitle2 = models.CharField(
        db_column="MusicTitle2", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    musictitle3 = models.CharField(
        db_column="MusicTitle3", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    musictitleen = models.CharField(
        db_column="MusicTitleEn", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    musictitlejp = models.CharField(
        db_column="MusicTitleJp", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    duration = models.CharField(
        db_column="Duration", max_length=10
    )  # Field name made lowercase.
    durationsec = models.CharField(
        db_column="DurationSec", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    composer = models.CharField(
        db_column="Composer", max_length=50
    )  # Field name made lowercase.
    lyricist = models.CharField(
        db_column="Lyricist", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    arranger = models.CharField(
        db_column="Arranger", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    price = models.IntegerField(
        db_column="Price", blank=True, null=True
    )  # Field name made lowercase.
    price2 = models.IntegerField(
        db_column="Price2", blank=True, null=True
    )  # Field name made lowercase.
    pricebak = models.IntegerField(
        db_column="PriceBak", blank=True, null=True
    )  # Field name made lowercase.
    musicurl_nrml = models.CharField(
        db_column="MusicUrl_nrml", max_length=350, blank=True, null=True
    )  # Field name made lowercase.
    musicurl = models.CharField(
        db_column="MusicUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    orifilename = models.CharField(
        db_column="OriFileName", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    musicfilesize = models.IntegerField(
        db_column="MusicFileSize", blank=True, null=True
    )  # Field name made lowercase.
    samplemusicurl = models.CharField(
        db_column="SampleMusicUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicurlwav = models.CharField(
        db_column="MusicUrlWav", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    orimusicfilenamewav = models.CharField(
        db_column="OriMusicFileNameWav", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    musicimg = models.CharField(
        db_column="MusicImg", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicimggettyori = models.CharField(
        db_column="MusicImgGettyOri", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicimggettyid = models.CharField(
        db_column="MusicImgGettyId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    musicimggettytitle = models.CharField(
        db_column="MusicImgGettyTitle", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    stemurl = models.CharField(
        db_column="StemUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    oristemfilename = models.CharField(
        db_column="OriStemFileName", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    movieurl = models.CharField(
        db_column="MovieUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    orimoviefilename = models.CharField(
        db_column="OriMovieFileName", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    youtubeurl = models.CharField(
        db_column="YoutubeUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    youtubevideoid = models.CharField(
        db_column="YoutubeVideoId", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    snsurl = models.CharField(
        db_column="SnsUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    instrumental = models.CharField(
        db_column="Instrumental", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    lyrics = models.TextField(
        db_column="Lyrics", blank=True, null=True
    )  # Field name made lowercase.
    bpm = models.IntegerField(
        db_column="Bpm", blank=True, null=True
    )  # Field name made lowercase.
    musicinfo = models.TextField(
        db_column="MusicInfo", blank=True, null=True
    )  # Field name made lowercase.
    filtertype = models.IntegerField(
        db_column="FilterType", blank=True, null=True
    )  # Field name made lowercase.
    copyrightassociation = models.CharField(
        db_column="CopyrightAssociation", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    hashtag = models.CharField(
        db_column="Hashtag", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    playcnt = models.IntegerField(db_column="PlayCnt")  # Field name made lowercase.
    downloadcnt = models.IntegerField(
        db_column="DownloadCnt"
    )  # Field name made lowercase.
    bookmarkcnt = models.IntegerField(
        db_column="BookmarkCnt"
    )  # Field name made lowercase.
    bookmarkbgmcnt = models.IntegerField(
        db_column="BookmarkBgmCnt"
    )  # Field name made lowercase.
    likecnt = models.IntegerField(db_column="LikeCnt")  # Field name made lowercase.
    recommendcnt = models.IntegerField(
        db_column="RecommendCnt"
    )  # Field name made lowercase.
    commentcnt = models.IntegerField(
        db_column="CommentCnt"
    )  # Field name made lowercase.
    arrangeyn = models.CharField(
        db_column="ArrangeYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    multifileyn = models.CharField(
        db_column="MultiFileYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    copyrightyn = models.CharField(
        db_column="CopyrightYn", max_length=1
    )  # Field name made lowercase.
    snsuseagreeyn = models.CharField(
        db_column="SnsUseAgreeYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    snsuseagreedate = models.DateTimeField(
        db_column="SnsUseAgreeDate", blank=True, null=True
    )  # Field name made lowercase.
    jointworkyn = models.CharField(
        db_column="JointWorkYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    jointworkconfirmationurl = models.CharField(
        db_column="JointWorkConfirmationUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    orijointworkconfirmationfilename = models.CharField(
        db_column="OriJointWorkConfirmationFileName",
        max_length=300,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    bgmyn = models.CharField(
        db_column="BGMYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    hiphopbeatyn = models.CharField(
        db_column="HiphopBeatYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    bgmrecommendyn = models.CharField(
        db_column="BGMRecommendYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    downloadfreepayyn = models.CharField(
        db_column="DownloadFreePayYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    freeyn = models.CharField(
        db_column="FreeYn", max_length=1
    )  # Field name made lowercase.
    soldyn = models.CharField(
        db_column="SoldYn", max_length=1
    )  # Field name made lowercase.
    useyn = models.CharField(
        db_column="UseYn", max_length=1
    )  # Field name made lowercase.
    delyn = models.CharField(
        db_column="DelYn", max_length=1
    )  # Field name made lowercase.
    delreason = models.CharField(
        db_column="DelReason", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    insdate = models.DateTimeField(
        db_column="InsDate", blank=True, null=True
    )  # Field name made lowercase.
    uptdate = models.DateTimeField(
        db_column="UptDate", blank=True, null=True
    )  # Field name made lowercase.
    approvalyn = models.CharField(
        db_column="ApprovalYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    approvaldate = models.DateTimeField(
        db_column="ApprovalDate", blank=True, null=True
    )  # Field name made lowercase.
    rejectyn = models.CharField(
        db_column="RejectYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    rejectdate = models.DateTimeField(
        db_column="RejectDate", blank=True, null=True
    )  # Field name made lowercase.
    rejectreason = models.CharField(
        db_column="RejectReason", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    sourceaudioexceptionyn = models.CharField(
        db_column="SourceAudioExceptionYn", max_length=1
    )  # Field name made lowercase.
    sourceaudioyn = models.CharField(
        db_column="SourceAudioYn", max_length=1
    )  # Field name made lowercase.
    sourceaudiouploadid = models.CharField(
        db_column="SourceAudioUploadId", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    sourceaudiouploaddate = models.DateTimeField(
        db_column="SourceAudioUploadDate", blank=True, null=True
    )  # Field name made lowercase.
    sourceaudiotrackid = models.CharField(
        db_column="SourceAudioTrackId", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    komcaid = models.CharField(
        db_column="KomcaId", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    distributionalbumidx = models.IntegerField(
        db_column="DistributionAlbumIdx", blank=True, null=True
    )  # Field name made lowercase.
    distributiontrackidx = models.IntegerField(
        db_column="DistributionTrackIdx", blank=True, null=True
    )  # Field name made lowercase.
    distributiontitleyn = models.CharField(
        db_column="DistributionTitleYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    snowyn = models.CharField(
        db_column="SnowYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    loopyn = models.CharField(
        db_column="LoopYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    aimakeyn = models.CharField(
        db_column="AIMakeYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    grade = models.IntegerField(
        db_column="Grade", blank=True, null=True
    )  # Field name made lowercase.
    monthlydownloadcnt = models.IntegerField(
        db_column="MonthlyDownloadCnt", blank=True, null=True
    )  # Field name made lowercase.
    highlightworkyn = models.CharField(
        db_column="HighlightWorkYn", max_length=1
    )  # Field name made lowercase.
    highlightyn = models.CharField(
        db_column="HighlightYn", max_length=1
    )  # Field name made lowercase.
    highlightstartsec = models.IntegerField(
        db_column="HighlightStartSec"
    )  # Field name made lowercase.
    prepaymentyn = models.CharField(
        db_column="PrepaymentYn", max_length=1
    )  # Field name made lowercase.
    prepayment = models.IntegerField(
        db_column="Prepayment"
    )  # Field name made lowercase.
    ishiphopbeat = models.CharField(
        db_column="IsHipHopBeat", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    hiphopsalemp3 = models.CharField(
        db_column="hiphopsaleMp3", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    hiphopsalewav = models.CharField(
        db_column="hiphopsaleWav", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    hiphopsalestem = models.CharField(
        db_column="hiphopsaleStem", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    stemtrackcnt = models.IntegerField(
        db_column="stemTrackCnt", blank=True, null=True
    )  # Field name made lowercase.
    hiphopkey = models.CharField(
        db_column="hiphopKey", max_length=2, blank=True, null=True
    )  # Field name made lowercase.
    hiphopscale = models.CharField(
        db_column="hiphopScale", max_length=3, blank=True, null=True
    )  # Field name made lowercase.
    buyerlengthchangeyn = models.CharField(
        db_column="buyerLengthChangeYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    bgmsaletooyn = models.CharField(
        db_column="BgmsaleTooYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    outsidesalesyn = models.CharField(
        db_column="outsideSalesYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    beatnotdelyn = models.CharField(
        db_column="beatNotDelYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    stemsoldyn = models.CharField(
        db_column="stemSoldYn", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    stemsolddate = models.DateTimeField(
        db_column="stemSoldDate", blank=True, null=True
    )  # Field name made lowercase.
    ismusician = models.CharField(
        db_column="Ismusician", max_length=1
    )  # Field name made lowercase.
    approvalbeatyn = models.CharField(
        db_column="ApprovalBeatYn", max_length=1
    )  # Field name made lowercase.
    approvalbeatdate = models.DateTimeField(
        db_column="ApprovalBeatDate", blank=True, null=True
    )  # Field name made lowercase.
    rejectbeatyn = models.CharField(
        db_column="RejectBeatYn", max_length=1
    )  # Field name made lowercase.
    rejectbeatdate = models.DateTimeField(
        db_column="RejectBeatDate", blank=True, null=True
    )  # Field name made lowercase.
    rejectbeatreason = models.CharField(
        db_column="RejectBeatReason", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicimgunsplashid = models.CharField(
        db_column="MusicImgUnsplashId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    musicimgunsplashtitle = models.CharField(
        db_column="MusicImgUnsplashTitle", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicimg2 = models.CharField(
        db_column="MusicImg2", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicimgunsplashid2 = models.CharField(
        db_column="MusicImgUnsplashId2", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    musicimgunsplashtitle2 = models.CharField(
        db_column="MusicImgUnsplashTitle2", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    lowmusicurl = models.CharField(
        db_column="LowMusicUrl", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    komcayn = models.CharField(
        db_column="komcaYn", max_length=1
    )  # Field name made lowercase.
    freechangeyn = models.CharField(
        db_column="freeChangeYn", max_length=1
    )  # Field name made lowercase.
    sourceaudioassetid = models.CharField(
        db_column="SourceAudioAssetId", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    shortformyn = models.CharField(
        db_column="shortformYn", max_length=1
    )  # Field name made lowercase.
    orimusicidx = models.IntegerField(
        db_column="oriMusicIdx", blank=True, null=True
    )  # Field name made lowercase.
    genre = models.CharField(
        db_column="Genre", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    mood = models.CharField(
        db_column="Mood", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    playsec = models.IntegerField(
        db_column="PlaySec", blank=True, null=True
    )  # Field name made lowercase.
    sunoyn = models.CharField(
        db_column="SunoYn", max_length=1
    )  # Field name made lowercase.
    musicurlaac = models.CharField(
        db_column="MusicUrlAac", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    musicurlcdn = models.CharField(
        db_column="MusicUrlCdn", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    openyn = models.CharField(
        db_column="OpenYn", max_length=1
    )  # Field name made lowercase.
    opendate = models.CharField(
        db_column="OpenDate", max_length=10, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = "Ct_Music"
