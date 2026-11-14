/**
 * Thin language pin (CANON_SPEC §10): English output. No duplicated math —
 * every kernel lives in ABCloudVerify.java; this only pins --lang en (it is
 * appended after the user's flags, so it wins over an explicit --lang).
 *
 * Build & run:  javac -encoding UTF-8 *.java && java ABCloudVerifyEn --zeros 50000
 * (JDK 11+ single-file: java ABCloudVerify.java --lang en ...)
 */
public class ABCloudVerifyEn {
    public static void main(String[] args) {
        String[] full = new String[args.length + 2];
        System.arraycopy(args, 0, full, 0, args.length);
        full[args.length] = "--lang";
        full[args.length + 1] = "en";
        ABCloudVerify.runMain(full);
    }
}
