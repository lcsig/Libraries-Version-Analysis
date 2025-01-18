# Libraries-Version-Analysis

Simple Project to Compare Between the Old Library and the New One to Check if the New Lib Doesn't Support or Deprecate Some Functions Leading to Regressions

### Output Example:

```bash
[-] Enter Old Lib Location: commons-io-2.4.jar
[-] Enter New Lib Location: commons-io-2.11.0.jar
============================================================
[+] Class ---> Charsets

	public static java.nio.charset.Charset toCharset(java.lang.String);
============================================================
[+] Class ---> ReverseComparator

	class org.apache.commons.io.comparator.ReverseComparator extends org.apache.commons.io.comparator.AbstractFileComparator implements java.io.Serializable {
	public org.apache.commons.io.comparator.ReverseComparator(java.util.Comparator<java.io.File>);
============================================================
[+] Class ---> AbstractFileFilter

	public abstract class org.apache.commons.io.filefilter.AbstractFileFilter implements org.apache.commons.io.filefilter.IOFileFilter {
============================================================
[+] Class ---> IOFileFilter

	public interface org.apache.commons.io.filefilter.IOFileFilter extends java.io.FileFilter,java.io.FilenameFilter {
============================================================
[+] Class ---> NameFileFilter

	public org.apache.commons.io.filefilter.NameFileFilter(java.lang.String[]);
============================================================
[+] Class ---> PrefixFileFilter

	public org.apache.commons.io.filefilter.PrefixFileFilter(java.lang.String[]);
============================================================
[+] Class ---> SuffixFileFilter

	public org.apache.commons.io.filefilter.SuffixFileFilter(java.lang.String[]);
============================================================
[+] Class ---> WildcardFileFilter

	public org.apache.commons.io.filefilter.WildcardFileFilter(java.lang.String[]);
============================================================
[+] Class ---> WildcardFilter

	public org.apache.commons.io.filefilter.WildcardFilter(java.lang.String[]);
============================================================
[+] Class ---> FilenameUtils

	public static boolean directoryContains(java.lang.String, java.lang.String) throws java.io.IOException;
	public static int indexOfExtension(java.lang.String);
	public static java.lang.String getExtension(java.lang.String);
	public static boolean isExtension(java.lang.String, java.lang.String[]);
============================================================
[+] Class ---> FileUtils

	public static java.io.File[] toFiles(java.net.URL[]);
	public static java.net.URL[] toURLs(java.io.File[]) throws java.io.IOException;
	public static boolean isSymlink(java.io.File) throws java.io.IOException;
============================================================
[+] Class ---> BOMInputStream

	final class org.apache.commons.io.input.BOMInputStream$1 implements java.util.Comparator<org.apache.commons.io.ByteOrderMark> {
	public int compare(org.apache.commons.io.ByteOrderMark, org.apache.commons.io.ByteOrderMark);
============================================================
[+] Class ---> IOCase

	public final class org.apache.commons.io.IOCase implements java.io.Serializable {
============================================================
[+] Class ---> IOUtils

	public static byte[] toByteArray(java.lang.String) throws java.io.IOException;
	public static java.lang.String toString(byte[]) throws java.io.IOException;
	public static java.lang.String toString(byte[], java.lang.String) throws java.io.IOException;
	public static org.apache.commons.io.LineIterator lineIterator(java.io.InputStream, java.nio.charset.Charset) throws java.io.IOException;
	public static org.apache.commons.io.LineIterator lineIterator(java.io.InputStream, java.lang.String) throws java.io.IOException;
	public static java.io.InputStream toInputStream(java.lang.CharSequence, java.lang.String) throws java.io.IOException;
	public static java.io.InputStream toInputStream(java.lang.String, java.lang.String) throws java.io.IOException;
============================================================
[+] Class ---> LineIterator

	public class org.apache.commons.io.LineIterator implements java.util.Iterator<java.lang.String> {
============================================================
[+] Class ---> FileEntry

	public void setChildren(org.apache.commons.io.monitor.FileEntry[]);
============================================================
[+] Class ---> ByteArrayOutputStream

	public class org.apache.commons.io.output.ByteArrayOutputStream extends java.io.OutputStream {
============================================================
[+] Class ---> ThresholdingOutputStream

	public abstract class org.apache.commons.io.output.ThresholdingOutputStream extends java.io.OutputStream {
============================================================
[+] Class ---> TaggedIOException

	public java.io.IOException getCause();
============================================================
[+] Class ---> ThreadMonitor

	public static java.lang.Thread start(long);
	public static java.lang.Thread start(java.lang.Thread, long);
	public static void stop(java.lang.Thread);
```

### Notes

- Updating a compilation path library:
   - If the project compiles successfully, then it is zero risk.
- Updating a runtime path library:
  - If it is a major version update, high-risk and potentional of braking things.
  - If minor version update, then it is low risk.
  - If revision version change, then it is almost no risk and just bug fixes.

## Buy me a Coffee: 
BTC: bc1q2kqvggm552h0csyr0awa2zepdapxdqnacw0z5w

![BTC](https://raw.githubusercontent.com/lcsig/API-Hooking/refs/heads/master/img/btc.png)
